import frame_window
from enum import Enum

class SlamState(Enum) :
    ERROR = -1
    INITIALIZING = 1
    CATCH = 2
    FAIL = 3

class SlamSystem:
    def __init__(self):
        self.state = SlamState.INITIALIZING
