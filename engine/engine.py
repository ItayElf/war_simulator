from context import Context
from engine.events import WAR_EVENT_TABLE
from outcome import Outcome
from random_utils import Dice, choose_with_ranges


class Engine:
    def __init__(self, context: Context) -> None:
        self.context = context

    def dispatch_event(self) -> Outcome:
        relative_score = self.context.score * (1 if self.context.initiative_at_side_a else -1)
        world_event_dice = Dice(100, modifier=relative_score)

        event = choose_with_ranges(WAR_EVENT_TABLE, world_event_dice)
        return event.apply(self.context)
