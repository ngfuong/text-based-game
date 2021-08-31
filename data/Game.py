from formatter.text_format import *


class Game:
    """
    This represents the world.
    Internally, we use a graph of Location objects and Item objects, which can be at a Location or in the Inventory.
    Each Location has a set of exits which are the Directions to which the player can move to get to an adjacent Location.
    The player can move from one Location to another Location via command "Go North".
    """

    def __init__(self, start_at):
        """
        :param start_at: the location in the game where the player starts
        :return: None
        """
        self.curr_location = start_at
        self.curr_location.has_been_visited = True
        self.inventory = {}
        self.print_commands = True

    def describe(self):
        """
        Describe the current game state by describing current Location, Exits and listing any Items in curr Location.
        :return:
        """
        self.describe_current_location()
        # Hide exits
        # self.describe_exits()
        self.describe_items()

    def describe_current_location(self):
        """
        List the current Location.
        :return:
        """
        print_bold(self.curr_location.description)

    def describe_exits(self):
        """
        List the Directions that the player can take to get to adjacent Locations.
        :return:
        """
        exits = []
        for exit in self.curr_location.connections.keys():
            exits.append(exit.capitalize())
        if len(exits) > 0:
            print_bold("Exits: ", end='')
            print_bold(*exits, sep=", ",)

    def describe_items(self):
        items = self.curr_location.items
        if len(items) > 0:
            print_bold("There is ", end='') if len(items) == 1 else print_bold("There are ", end='')
            print_bold(", ".join(items[item_name].description for item_name in items)+'.')
            # for item_name in self.curr_location.items:
            #     item = self.curr_location.items[item_name]
            #     print(item.description)
            #     #print(*exits, sep=", ", )
            #     if self.print_commands:
            #         special_commands = item.get_commands()
            #         for cmd in special_commands:
            #             print('\t', cmd)

    def add_to_inventory(self, item):
        """
        Add an item to the player's Inventory.
        :param item:
        :return:
        """
        self.inventory[item.name] = item

    def is_in_inventory(self, item):
        return item.name in self.inventory

    def get_items_in_scope(self):
        """
        :return: A list of items in the current Location and in the Inventory.
        """
        items_in_scope = []
        for item_name in self.curr_location.items:
            items_in_scope.append(self.curr_location.items[item_name])
        for item_name in self.inventory:
            items_in_scope.append(self.inventory[item_name])
        return items_in_scope
