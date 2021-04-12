class Location:
    """
    Locations are the in-game places that a player can visit.
    Internally, they are represented as nodes in a graph.
    Each Location stores its description, its Items and Connections to adjacent Locations.
    The Connections is a dictionary whose keys are Directions and
    whose values are the adjacent Locations in the respective Directions.
    The travel_descriptions also has Directions as keys,
    and its values are an optional short description of traveling to that Location.
    """
    def __init__(self, name, description, end_game=False):
        """
        :param name: short name for the Location
        :param description: description of the Location
        :param end_game: if entering this Location should end the game
        """
        self.name = name
        self.description = description
        self.end_game = end_game
        # A Dict mapping Directions to its respective adjacent Locations
        self.connections = {}
        # A Dict mapping Directions to the text description of the path leading there
        self.travel_descriptions = {}
        # A Dict mapping Directions to Block object in that Direction
        self.blocks = {}
        # A Dict mapping Item name to Item objects present in this Location
        self.items = {}
        # Flag that is set to True once this Location has been visited
        self.has_been_visited = False

    def add_connection(self, direction, connected_location, travel_description=""):
        """
        Add a connection from the current Location to a connected Location
        :param direction: a String that a player can use to get to the connected location.
                        if it is primary, auto make a connection in the reverse Direction.
        :param connected_location:
        :param travel_description: A Dict mapping Directions to the text description of the path leading there
        :return:
        """
        self.connections[direction] = connected_location
        self.travel_descriptions[direction] = travel_description
        if direction == "north":
            connected_location.connections["south"] = self
            connected_location.travel_description["south"] = ""
        if direction == "south":
            connected_location.connections["north"] = self
            connected_location.travel_description["north"] = ""
        if direction == "east":
            connected_location.connections["west"] = self
            connected_location.travel_description["west"] = ""
        if direction == "west":
            connected_location.connections["east"] = self
            connected_location.travel_description["east"] = ""
        if direction == "up":
            connected_location.connections["down"] = self
            connected_location.travel_description["down"] = ""
        if direction == "down":
            connected_location.connections["up"] = self
            connected_location.travel_description["up"] = ""
        if direction == "in":
            connected_location.connections["out"] = self
            connected_location.travel_description["out"] = ""
        if direction == "out":
            connected_location.connections["in"] = self
            connected_location.travel_description["in"] = ""

    def add_item(self, name, item):
        """
        Put an Item in this Location.
        :param name:
        :param item:
        :return:
        """
        self.items[name] = item

    def remove_item(self, item):
        """
        Remove and Item from this Location (i.e. the player picks the Item up)
        :param item:
        :return:
        """
        self.items.pop(item.name)

    def get_block_description(self, direction):
        """
        Check if there is an obstacle in this Direction
        :param direction:
        :return: block_description
        """
        if not direction in self.blocks:
            return ""
        else:
            (block_description, preconditions) = self.blocks[direction]
            return block_description

    def add_block(self, blocked_direction, block_description, preconditions):
        """
        Create an obstacle that prevents a player from moving into the blocked Location
        until the preconditions are all met.
        :param blocked_direction:
        :param block_description:
        :param preconditions:
        :return:
        """
        self.blocks[blocked_direction] = (blocked_direction, preconditions)

