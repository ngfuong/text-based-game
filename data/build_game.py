from . import *


def build_game():
    # Locations
    cottage = Location("Cottage", "You are standing in a small cottage.")
    garden_path = Location("Garden Path", "You are standing on a lush garden path. There is a cottage here.")
    cliff = Location("Cliff",
                     "There is a steep cliff here. You fall off the cliff and lose the game. THE END.",
                     end_game=True)
    fishing_pond = Location("Fishing Pond", "You are at the edge of a small fising pond.")

    # Connections
    cottage.add_connection("out", garden_path)
    garden_path.add_connection("west", cliff)
    garden_path.add_connection("south", fishing_pond)

    # Items that can be pick up
    fishing_pole = Item("pole", "a fishing pole", "A SIMPLE FISHING POLE", start_at=cottage)
    potion = Item("potion", "a poisonous potion", "IT'S BRIGHT GREEN AND STEAMING",
                  start_at=cottage,
                  take_text="As you get near the potion, the fumes cause you to faint and lose the game. THE END.")
    rosebush = Item("rosebush", "a rosebush", "THE ROSEBUSH CONTAINS A SINGLE RED ROSE. IT IS BEAUTIFUL",
                    start_at=garden_path)
    rose = Item("rose", "a red rose", "IT SMELLS GOOD", start_at=None)
    fish = Item("fish", "a dead fish", "IT SMELLS TERRIBLE", start_at=None)

    # Items that cannot be pick up
    pond = Item("pond", "a small fishing pond", "THERE ARE FISH IN THE POND", start_at=fishing_pond, gettable=False)

    # Add special functions to items
    rosebush.add_action("pick rose", add_item_to_inventory, (rose, "You pick the lone rose from the rosebush.",
                                                             "You already picked the rose."))
    rose.add_action("smell rose", describe_something, ("It smells sweet."))
    pond.add_action("catch fish", describe_something,
                    ("You reach into the pond and try to catch a fish with your hands, but they are too fast"))
    pond.add_action("catch fish with pole",
                    add_item_to_inventory, (fish,
                                            "You dip your hook into the pond and catch a fish",
                                            "You weren't able to catch any other fish."),
                    preconditions={"inventory_contains": fishing_pole})
    fish.add_action("eat fish",
                    end_game,
                    ("That's disgusting! It's raw! And definitely not sashima-grade! But you've won this version of the game. THE END."))

    return Game(cottage)