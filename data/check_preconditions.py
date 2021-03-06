"""
In text-based adventure game, it is common to block a player's progress by creating blocks that prevents them from
moving from a Location to another.
"""
from formatter.text_format import *


def check_preconditions(preconditions, game, print_failure_message=True):
    """
    Check if the preconditions are met.
    :param preconditions:
    :param game:
    :param print_failure_message:
    :return:
    """
    all_conditions_met = True
    for condition in preconditions:
        if condition == "inventory_contains":
            item = preconditions[condition]
            # TODO: Change this to modify game dynamics
            if not game.is_in_inventory(item):
                all_conditions_met = False
                if print_failure_message:
                    print_italic("You try but it seems like not have the correct item(s).")
        if condition == "in_location":
            location = preconditions[condition]
            if not game.curr_location == location:
                all_conditions_met = False
                if print_failure_message:
                    print_italic("You try but it seems like you are not in the correct location.")
        if condition == "location_has_item":
            item = preconditions[condition]
            if not item.name in game.curr_location.items:
                all_conditions_met = False
                if print_failure_message:
                    print_italic("It seems like the item is not in this location.")
        # TODO: Add other kind of conditions
    return all_conditions_met



