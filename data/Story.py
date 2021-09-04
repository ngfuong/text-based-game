from enum import Enum


class Story(Enum):
    def __init__(self, day=None):
        if day is None:
            self.day = 1
        else:
            self.day = day
