"""
Implementation of a Stack-based FSM
"""


class StackFSM:
    def __init__(self):
        # TODO: check back on this
        self.stack = []

    def _get_curr_state(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[len(self.stack) - 1]

    def update(self):
        curr_state = self._get_curr_state()

        if curr_state is not None:
            curr_state()

    def pop_state(self):
        return self.stack.pop()

    def push_state(self, new_state):
        if self._get_curr_state() != new_state:
            self.stack.append(new_state)
