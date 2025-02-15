from abc import ABC, abstractmethod
from enum import IntEnum


class State(IntEnum):
    """
    Basic enum for representing state of an item in OBS. `bool(value)` is
    guaranteed to provide the expected semantics for DISABLED (False) and
    ENABLED (True).
    """
    UNKNOWN = -1
    DISABLED = 0
    ENABLED = 1


class MixinBase(ABC):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._current_state: State = State.UNKNOWN

    @property
    def current_state(self) -> State:
        return self._current_state

    @current_state.setter
    def current_state(self, val: int | State):
        if isinstance(val, int):
            val = State(val)

        self._current_state = val

    @abstractmethod
    def next_state(self) -> State:
        pass
