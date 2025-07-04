from context import Context
from engine.engine_logger import EngineLogger
from engine.events import PEACE_OUTCOME_TABLE, WAR_EVENT_TABLE
from outcome import Outcome
from random_utils import Dice, choose_with_ranges


class Engine:
    def __init__(self, context: Context) -> None:
        self.context = context
        self.logger = EngineLogger(context)

    def dispatch_event(self) -> Outcome:
        relative_score = self.context.score * (1 if self.context.initiative_at_side_a else -1)
        world_event_dice = Dice(100, modifier=relative_score)

        event = choose_with_ranges(WAR_EVENT_TABLE, world_event_dice, ignore_limits=True)
        return event.apply(self.context)

    def apply_outcome(self, outcome: Outcome):
        self.context.days_passed += outcome.days_passed
        self.context.score += outcome.score_change * (1 if self.context.initiative_at_side_a else -1)

        if outcome.did_initiative_change:
            self.context.initiative_at_side_a = not self.context.initiative_at_side_a

    def progress_by_one_turn(self) -> Outcome:
        """
        Dispatches and applies one event
        """
        outcome = self.dispatch_event()
        self.apply_outcome(outcome)
        self.logger.log_outcome(outcome)
        return outcome

    def get_peace_outcome(self) -> str:
        """
        Returns a string representing the peace's outcome
        """
        score = abs(self.context.score)
        peace_outcome_dice = Dice(100, modifier=score)

        return choose_with_ranges(PEACE_OUTCOME_TABLE, peace_outcome_dice, ignore_limits=True)

    def simulate(self):
        """
        Simulates until there is a clear winner or a piece offer occurs
        """
        while -100 < self.context.score < 100:
            self.progress_by_one_turn()

        outcome = self.get_peace_outcome()
        self.logger.log_peace(outcome)
