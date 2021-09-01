import formatter.text_format
from data.check_preconditions import check_preconditions


class NPC:
    """
    Non-player Characters (NPC) are beings in game that player can interact with.
    The location of the NPC should change according to the story of the game.
    E.g: when a story flag is triggered
    Player can interact with the NPC and converse with them.
    """
    def __init__(self, name, genre, description, location, interact_text=""):
        """
        :param location: the location in the game where the NPC is located
        :param genre: the genre of the NPC (he/she/they/it)
        :return: none
        """
        self.name = name
        self.pronoun = genre
        self.description = description
        self.location = location
        if interact_text == "":
            self.interact_text = "You try to interact with {name} but {pronoun} does not react."\
                .format(name=self.name, pronoun=self.pronoun)

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
            formatter.text_format.print_italic("You cannot do that. Try something else.")
        return end_game
