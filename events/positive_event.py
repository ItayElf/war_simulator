from context import Context
from events.event import Event
from events.severity import SEVERITY_DAYS_DICE, SEVERITY_RANGES, SEVERITY_SCORE
from outcome import Outcome
from random_utils import choose_with_ranges


class PositiveEvent(Event):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def apply(self, context: Context) -> Outcome:
        severity = self._get_severity()
        return Outcome(
            f"{self.name} ({severity.name.title()}).",
            SEVERITY_SCORE[severity],
            SEVERITY_DAYS_DICE[severity].roll(),
            did_initiative_change=False,
        )

    @staticmethod
    def _get_severity():
        return choose_with_ranges(SEVERITY_RANGES)
