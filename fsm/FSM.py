"""
Implementation of a finite state machine (FSM)
"""


class FSM:
    def __init__(self, state):
        """
        :param: activeState is a pointer to the currently active function
        """
        # TODO: check back on this
        self.activeState = state

    def set_state(self, new_state):
        """
        This will transition the FSM to a new state by pointing the activeState
        to a new state function.
        """
        self.activeState = new_state

    def update(self):
        """
        This function calls the activeState function .
        This should be invoked every frame game/user interaction
        so that it can call the function pointed by the activeState property.
        """
        if self.activeState is not None:
            self.activeState()
