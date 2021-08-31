"""
Format output text of a game
"""


def print_italic(*args, **kwargs):
    text = ""
    for arg in args:
        text = arg
    print(__italic(text), **kwargs)


def __italic(text):
    return "\x1B[3m" + text + "\x1B[0m"


def print_bold(*args, **kwargs):
    text = ""
    for arg in args:
        text = arg
    print(__bold(text), **kwargs)


def __bold(text):
    return "\033[1m" + text + "\033[0m"
