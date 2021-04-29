class Parser:
    """
    This handles the player's input.
    The player writes commands and the Parser performs natural language understanding
    in order to interpret what the player intended, and how that intent is reflected
    in the simulated world.
    """
    def __init__(self, game):
        """
        :param game: a pointer to the game
        """
        # A list of all the commands that the player has issued.
        self.command_history = []
        self.game = game

    def get_player_intent(self, command):
        # Comma-separated sequence of command
        if "," in command:
            return "sequence"

        # Check for direction intent
        elif self.get_direction(command):
            return "direction"

        # TODO: Consider changing this
        # Redescribe the environment (Location)
        elif command == "look" or command == "l":
            return "redescribe"

        # Examine
        elif "examine" in command or command.startswith("x "):
            return "examine"

        # Take Item
        elif "take" in command:
            return "take"

        # Drop Item
        elif "drop" in command:
            return "drop"

        # Check inventory
        elif "inventory" in command or command == "i":
            return "inventory"

        # Special commands
        else:
            for item in self.game.get_items_in_scope():
                special_commands = item.get_commands()
                for special_command in special_commands:
                    if command == special_command:
                        return "special"

    def parse_command(self, command):
        """
        Intents are functions that can be executed.
        By default, none of the intents ends the game.
        The following are ways this flag can be changed to True:
        * Going to a certain Location
        * Triggering a certain Special Command
        * Picking up a certain Item
        :param command: user command
        :return: whether the game ends or not
        """
        # Add this command to history
        self.command_history.append(command)
        end_game = False

        # TODO: Make the parser able to handle tokens instead of commands
        intent = self.get_player_intent(command)
        if intent == "direction":
            end_game = self.go_in_direction(command)
        elif intent == "redescribe":
            self.game.describe()
        elif intent == "examine":
            self.examine(command)
        elif intent == "take":
            end_game = self.take(command)
        elif intent == "drop":
            self.drop(command)
        elif intent == "inventory":
            self.check_inventory(command)
        elif intent == "special":
            end_game = self.run_special_command(command)
        elif intent == "sequence":
            end_game = self.execute_sequence(command)
        else:
            print("Not sure what you want to do.")

        return end_game

    """
    Intent Functions
    """
    def go_in_direction(self,command):
        """
        The user wants to go in some Direction
        :param command:
        :return: if the game ends
        """
        direction = self.get_direction(command)
        if direction:
            if direction in self.game.curr_location.connections:
                if self.game.curr_location.is_blocked(direction, self.game):
                    print(self.game.curr_location.get_blocked_description(direction))
                else:
                    self.game.curr_location = self.game.curr_location.connections[direction]

                    if self.game.curr_location.end_game:
                        self.game.describe_current_location()
                    else:
                        self.game.describe()

            else:
                print("You cannot travel in that direction. Try something else.")
        return self.game.curr_location.end_game

    def check_inventory(self, command):
        """
        The player wants to check their inventory
        :param command:
        :return:
        """
        if len(self.game.inventory) == 0:
            print("Your inventory is empty.")
        else:
            descriptions = []
            for item_name in self.game.inventory:
                item = self.game.inventory[item_name]
                descriptions.append(item.description)
            print("You have:", end=' ')
            print(*descriptions, sep=", ",)

    def examine(self, command):
        """
        The player wants to examine something
        :param command:
        :return:
        """
        # Item in command matches items in current Location
        for item_name in self.game.curr_location.items:
            if item_name in command:
                item = self.game.curr_location.items[item_name]
                if item.examine_text:
                    # Describe item in Location and bypass checking item in Inventory
                    print(item.examine_text)
                    return

        # Item in command matches items in Inventory
        for item_name in self.game.inventory:
            if item_name in command:
                item = self.game.inventory[item_name]
                if item.examine_text:
                    # Describe item in Inventory
                    print(item.examine_text)
                    return

    def take(self, command):
        """
        The player wants to put something in their inventory
        :param command:
        :return: whether the game ends
        """
        matched_item = False
        end_game = False

        # Check if item in command matches any item of current Location:
        for item_name in self.game.curr_location.items:
            # Matched
            if item_name in command:
                item = self.game.curr_location.items[item_name]
                if item.gettable:
                    self.game.add_to_inventory(item)
                    self.game.curr_location.remove_item(item)
                    print(item.take_text)
                    end_game = item.end_game
                else:
                    print("You cannot take this item.")
                    break
                matched_item = True
                break

        # Not matched
        if not matched_item:
            print("You cannot find this item.")

        return end_game

    def drop(self, command):
        """
        The player wants to remove something from their Inventory
        :param command:
        :return:
        """
        matched_item = False

        # Item in command matches items in Inventory
        if not matched_item:
            for item_name in self.game.inventory:
                if item_name in command:
                    matched_item = True
                    item = self.game.inventory[item_name]
                    self.game.curr_location.add_item(item_name, item)
                    self.game.inventory.pop(item_name)
                    print('You successfully drop this item.')
                    break

        # No match
        if not matched_item:
            print("You don't have that item.")

    def run_special_command(self, command):
        """
        Run a special command associated with one of the Items in this Locations
        or in the player's Inventory.
        :param command:
        :return:
        """
        for item in self.game.get_items_in_scope():
            special_commands = item.get_commands()
            for special_command in special_commands:
                if command == special_command:
                    # do_action is a special function in the frontend built - in lib
                    return item.do_action(special_command, self.game)

    def execute_sequence(self, command):
        for cmd in command.split(","):
            cmd = cmd.strip()
            self.parse_command(cmd)

    def get_direction(self, command):
        directions = ["east", "west", "south", "north", "up", "down", "out", "in"]
        direction_dispatch = {"go {direction}".format(direction=direction): direction for direction in directions}

        exits = self.game.curr_location.connections.keys()
        exit_dispatch = {"go {exit}".format(exit=exit): exit for exit in exits}

        for direction in direction_dispatch.keys():
            if direction in command:
                return direction_dispatch[direction]

        for exit in exit_dispatch.keys():
            if exit in command:
                return exit_dispatch[exit]

        return None
