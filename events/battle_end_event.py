from copy import deepcopy
import random
from battle import SCORE_INCREASE_FROM_WIN, Battle
from context import Context
from events.event import Event
from exceptions import RerollException
from outcome import Outcome


_BATTLE_END_REASONS = [
    "third party intervention",
    "exhaustion of forces",
    "reinforcements arrival",
    "a disease outbreak",
    "command failure or death",
    "a strategic withdrawal",
    "weather or terrain intervention",
    "a prophetic sign or religious event ",
    "supply lines cut",
    "a rebellion",
]


class BattleEndEvent(Event):
    _SCORE_THRESHOLD = 4

    def apply(self, context: Context) -> Outcome:
        active_battles = [b for b in context.battles if b.is_active]
        if not active_battles:
            raise RerollException()

        battle = deepcopy(random.choice(active_battles))
        battle.is_active = False
        score_change = self._get_score_change(battle)
        description = (
            f"Battle {battle.name!r} was ended after {context.days_passed - battle.started_at} "
            f"days due to {random.choice(_BATTLE_END_REASONS)}"
        )

        if score_change:
            winner = context.side_a if battle.score > 0 else context.side_b
            description += f". This is considered as a win for {winner}."

        return Outcome(
            description,
            score_change,
            days_passed=0,
            did_initiative_change=False,
            battle_change=battle,
        )

    @staticmethod
    def _get_score_change(battle: Battle) -> int:
        if battle.score < BattleEndEvent._SCORE_THRESHOLD:
            return 0

        return SCORE_INCREASE_FROM_WIN[battle.severity]
