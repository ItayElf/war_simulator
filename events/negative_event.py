from context import Context
from events.event import Event
from events.severity import SEVERITY_DAYS_DICE, SEVERITY_RANGES, SEVERITY_SCORE, Severity
from outcome import Outcome
from random_utils import Dice, choose_with_ranges


class NegativeEvent(Event):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def apply(self, context: Context) -> Outcome:
        severity = self._get_severity()
        return Outcome(
            f"{self.name} ({severity.name.title()})",
            SEVERITY_SCORE[severity] * (-1),
            SEVERITY_DAYS_DICE[severity].roll(),
            self._did_initiative_change(severity),
        )

    @staticmethod
    def _did_initiative_change(severity: Severity):
        if severity is Severity.MINOR:
            return False

        if severity is Severity.MODERATE:
            return Dice(2).roll() == 1

        return True

    @staticmethod
    def _get_severity():
        return choose_with_ranges(SEVERITY_RANGES)
