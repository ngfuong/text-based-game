from formatter.text_format import *


def add_item_to_inventory(game, *args):
    """
    Add a newly created Item into your Inventory
    :param game:
    :param args:
    :return:
    """
    (item, action_description, already_done_description) = args[0]
    if not game.is_in_inventory(item):
        print_bold(action_description)
        game.add_to_inventory(item)
        print_italic("You've just got a {item}.".format(item=item.name))
    else:
        print_italic(already_done_description)
    return False


def describe_something(game, *args):
    """
    Describe an Item
    :param game:
    :param args:
    :return:
    """
    (description) = args[0]
    print_bold(description)
    return False


def destroy_item(game, *args):
    """
    Remove an Item from the game by setting its Location to None
    :param game:
    :param args:
    :return:
    """
    (item, action_description, already_done_description) = args[0]
    if game.is_in_inventory(item):
        game.inventory.pop(item.name)
        print_bold(action_description)
    elif item.name in game.curr_location.items:
        game.curr_location.remove_item(item)
        print_bold(action_description)
    else:
        print_bold(already_done_description)
    return False


def end_game(game, *args):
    """
    Ends the game
    :param game:
    :param args:
    :return: whether the game ends or not
    """
    end_message = args[0]
    print_bold(end_message)
    return True

