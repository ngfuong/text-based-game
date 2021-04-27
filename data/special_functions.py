def add_item_to_inventory(game, *args):
    """
    Add a newly created Item into your Inventory
    :param game:
    :param args:
    :return:
    """
    (item, action_description, already_done_description) = args[0]
    if not game.is_in_inventory(item):
        print(action_description)
        game.add_to_inventory(item)
        print("You've just got a {item}.".format(item=item.name))
    else:
        print(already_done_description)
    return False


def describe_something(game, *args):
    """
    Describe an Item
    :param game:
    :param args:
    :return:
    """
    (description) = args[0]
    print(description)
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
        print(action_description)
    elif item.name in game.curr_location.items:
        game.curr_location.remove_item(item)
        print(action_description)
    else:
        #TODO: WHat the hell
        print(already_done_description)
    return False


def end_game(game, *args):
    """
    Ends the game
    :param game:
    :param args:
    :return: whether the game ends or not
    """
    end_message = args[0]
    print(end_message)
    return True

