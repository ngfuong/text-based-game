from data.Game import Game
from data.Item import Item
from data.Location import Location
from data.special_functions import *
from nlp.generate_commands import *


def build_game():
    """Edit this to customize the story of the game."""
    # Locations
    lounge = Location("Lookout Tower",
                      "You are standing in the lounge of the lookout tower.")

    lookout_spot = Location("Lookout Spot",
                            "You are standing in the middle of the lookout spot, on the upper level of the tower.")
    yard = Location("Outer Yard",
                    "You are in the outer yard of the tower.")
    woods = Location("Woods",
                     "You wander into the woods near the tower.")

    # Connections
    lounge.add_connection("up", lookout_spot)
    lounge.add_connection("out", yard)
    yard.add_connection("out", woods)
    yard.add_connection("in", lounge)
    woods.add_connection("in", yard)
    lookout_spot.add_connection("down", lounge)

    # Items that can be pick up
    fishing_pole = Item("pole", "a fishing pole", "It's just a simple fishing pole.",
                        start_at=cottage)
    potion = Item("potion", "a bottle of potion", "It's bright green and steaming.",
                  start_at=cottage,
                  take_text="As you get near the potion, the fumes cause you to faint and lose the game. THE END.",
                  end_game=True)
    rosebush = Item("rosebush", "a rosebush", "The rosebush contains a single red rose. It is beautiful.",
                    start_at=garden_path)
    rose = Item("rose", "a red rose", "It smells good.")
    fish = Item("fish", "a fish", "The fish is dead. It smells terrible.")

    # Items that cannot be pick up
    pond = Item("pond", "a small fishing pond", "There are fish swimming in the pond.",
                start_at=fishing_pond,
                gettable=False)

    """
    Add special functions to items
    """
    # Generating dictionary of alternative commands
    commands = ["pick rose",
                "smell rose",
                "catch fish",
                "catch fish with pole",
                "eat fish"]
    # RUN THIS TO CREATE LOCAL ANNOTATIONS
    # senses, hypernyms, hyponyms = generate_annotations(commands)
    # save_to_file(senses, hypernyms, hyponyms)
    cmd_dict = generate_command_dict(commands)
    # Making alternatives work
    for cmd in cmd_dict["pick rose"]:
        rosebush.add_action(cmd, add_item_to_inventory,
                            (rose, "You pick the lone rose from the rosebush.", "You already picked the rose."))
    for cmd in cmd_dict["smell rose"]:
        rose.add_action(cmd, describe_something,
                        ("It smells sweet."))
    for cmd in cmd_dict["catch fish"]:
        pond.add_action(cmd, describe_something,
                        ("You reach into the pond and try to catch a fish with your hands, but they are too fast."))
    for cmd in cmd_dict["catch fish with pole"]:
        pond.add_action(cmd,
                        add_item_to_inventory,
                        (fish, "You dip your hook into the pond and catch a fish.",
                         "You weren't able to catch any other fish."),
                        preconditions={"inventory_contains": fishing_pole})
    for cmd in cmd_dict["eat fish"]:
        fish.add_action(cmd, end_game,
                        (
                            "That's disgusting! It's raw! And definitely not sashima-grade! But you've won this version of the game. THE END."))

    return Game(cottage)
