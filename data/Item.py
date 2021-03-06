from data.check_preconditions import check_preconditions
from formatter.text_format import *


class Item:
    """
    Items are objects that a player can take or examine.
    """
    def __init__(self, name, description, examine_text="", take_text="", start_at=None, gettable=True, end_game=False):
        """
        :param name: Item name
        :param description: default description of Item
        :param examine_text: detailed description when the player examines the Item
        :param take_text: text displayed when the player takes the Item
        :param start_at: the initial Location of the Item
        :param gettable: indicates whether the player can take the object and put it in their Inventory
        :param end_game: True if entering this Location should end the game
        """
        self.name = name
        self.description = description
        if examine_text == "":
            self.examine_text = "You do not see anything special."
        else:
            self.examine_text = examine_text
        if take_text == "":
            self.take_text = "You have taken the {name}.".format(name=self.name)
        else:
            self.take_text = take_text
        self.gettable = gettable
        self.end_game = end_game

        if start_at:
            start_at.add_item(name,self)
        self.commands = {}

    def get_commands(self):
        """
        :return: a list of special commands associated with the Item
        """
        return self.commands.keys()

    def add_action(self, command_text, function, arguments, preconditions=None):
        """
        Add a special action associated with the Item
        :param command_text:
        :param function: this function will be called
        :param arguments: argument for the respective function
        :param preconditions:
        :return:
        """
        if preconditions is None:
            preconditions = {}
        self.commands[command_text] = (function, arguments, preconditions)

    def do_action(self, command_text, game):
        """
        Performs a special action associated with the Item
        :param command_text:
        :param game:
        :return: whether the game ends or not
        """
        end_game = False
        if command_text in self.commands:
            function, arguments, preconditions = self.commands[command_text]
            if check_preconditions(preconditions, game):
                end_game = function(game, arguments)
        else:
            print_italic("You cannot do that. Try something else.")
        return end_game



