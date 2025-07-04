from abc import ABC, abstractmethod

from context import Context
from outcome import Outcome


class Event(ABC):
    @abstractmethod
    def apply(self, context: Context) -> Outcome:
        pass
