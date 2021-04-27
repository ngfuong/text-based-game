from data.Game import Game
from data.Item import Item
from data.Location import Location
from data.special_functions import *
from nlp.generate_commands import generate_command_list


def build_game():
    # Locations
    cottage = Location("Cottage", "You are standing in a small cottage.")
    garden_path = Location("Garden Path", "You are standing on a lush garden path. There is a cottage here.")
    cliff = Location("Cliff",
                     "There is a steep cliff here. You fall off the cliff and lose the game. THE END.",
                     end_game=True)
    fishing_pond = Location("Fishing Pond", "You are at the edge of a small fishing pond.")

    # Connections
    cottage.add_connection("out", garden_path)
    garden_path.add_connection("west", cliff)
    garden_path.add_connection("south", fishing_pond)

    # Items that can be pick up
    fishing_pole = Item("pole", "a fishing pole", "It's just a simple fishing pole", start_at=cottage)
    potion = Item("potion", "a poisonous potion", "It's bright green and steaming",
                  start_at=cottage,
                  take_text="As you get near the potion, the fumes cause you to faint and lose the game. THE END.")
    rosebush = Item("rosebush", "a rosebush", "The rosebush contains a single red rose. It is beautiful",
                    start_at=garden_path)
    rose = Item("rose", "a red rose", "It smells good", start_at=None)
    fish = Item("fish", "a dead fish", "It smells terrible", start_at=None)

    # Items that cannot be pick up
    pond = Item("pond", "a small fishing pond", "THERE ARE FISH IN THE POND", start_at=fishing_pond, gettable=False)

    # Add special functions to items
    rosebush.add_action("pick rose", add_item_to_inventory, (rose,
                                                             "You pick the lone rose from the rosebush.",
                                                             "You already picked the rose."))
    rose.add_action("smell rose", describe_something, ("It smells sweet."))

    for cmd in generate_command_list("catch fish"):
        pond.add_action(cmd, describe_something,
                        ("You reach into the pond and try to catch a fish with your hands, but they are too fast."))

    pond.add_action("catch fish with pole",
                    add_item_to_inventory, (fish,
                                            "You dip your hook into the pond and catch a fish.",
                                            "You weren't able to catch any other fish."),
                    preconditions={"inventory_contains": fishing_pole})
    fish.add_action("eat fish",
                    end_game,
                    (
                        "That's disgusting! It's raw! And definitely not sashima-grade! But you've won this version of the game. THE END."))

    return Game(cottage)
