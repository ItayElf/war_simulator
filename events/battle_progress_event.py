from copy import deepcopy
import random
from battle import SCORE_INCREASE_FROM_WIN, BattleSeverity
from context import Context
from events.event import Event
from exceptions import RerollException
from outcome import Outcome
from random_utils import Dice, choose_with_ranges

_BATTLE_PROGRESS_TABLE = {
    range(1, 2): ("catastrophic collapse", -3, 100),
    range(2, 4): ("collapse", -2, 100),
    range(4, 7): ("major setback", -1, 50),
    range(7, 11): ("minor setback", -1, 25),
    range(11, 14): ("stalemate", 0, 0),
    range(14, 18): ("minor advance", 1, 0),
    range(18, 21): ("major advance", 1, 0),
    range(21, 23): ("critical push", 2, 0),
    range(23, 25): ("crushing blow", 3, 0),
}

_FALLOUT_OPTIONS = [
    "a champion to fall on the battlefield, or a beloved leader to lose hope",
    "a physical banner to be captured or destroyed, or a symbol of hope to be shattered",
    "a scandal to erupt within the ranks, or cultural shame to weaken morale",
    "civilians to rebel, or key allies to withdraw support or lose faith",
    "a real fortress to be captured, or a spiritual sanctuary, safe haven, or trade route to be compromised",
    "a commander to be injured or slain, or a political leader to suffer mental breakdown or betrayal",
    "religious fervor to wane, or ideological conviction to falter among troops",
    "actual traitors or spies to be revealed, or distrust and paranoia to spread",
    "ghosts or curses to plague the area, or past failures to weigh heavily on morale",
    "factions to splinter off, or dissent to grow within a population or army",
]

_SCORE_THRESHOLD = {
    BattleSeverity.SKIRMISH: 3,
    BattleSeverity.ENGAGEMENT: 6,
    BattleSeverity.CAMPAIGN: 10,
    BattleSeverity.DECISIVE_CLASH: 15,
}

_DAYS_PASSED_DICE_TABLE = {
    BattleSeverity.SKIRMISH: Dice(3),
    BattleSeverity.ENGAGEMENT: Dice(5, modifier=3),
    BattleSeverity.CAMPAIGN: Dice(6, modifier=8),
    BattleSeverity.DECISIVE_CLASH: Dice(6, modifier=14),
}


class BattleProgressEvent(Event):
    def apply(self, context: Context) -> Outcome:
        active_battles = [b for b in context.battles if b.is_active]
        if not active_battles:
            raise RerollException()

        battle = deepcopy(random.choice(active_battles))
        relative_score = battle.score * (1 if context.initiative_at_side_a else -1)
        outcome, change, initiative_flip_chance = choose_with_ranges(
            _BATTLE_PROGRESS_TABLE, Dice(10, 2, relative_score), ignore_limits=True
        )

        battle.score += change * (1 if context.initiative_at_side_a else -1)
        did_flip_initiative = random.randint(1, 100) <= initiative_flip_chance

        initiator = context.side_a if context.initiative_at_side_a else context.side_b
        initiator_text = f" for {initiator}" if change else ""
        description = f"Battle {battle.name!r} was progressed, leading to a {outcome}{initiator_text}."

        if did_flip_initiative:
            description += f" This caused {random.choice(_FALLOUT_OPTIONS)}."

        score_change = 0
        if abs(battle.score) >= _SCORE_THRESHOLD[battle.severity]:
            battle.is_active = False
            winner = context.side_a if battle.score > 0 else context.side_b
            description += (
                f" The battle was therefore ended after {context.days_passed - battle.started_at} days "
                f"and won by {winner}."
            )
            score_change = SCORE_INCREASE_FROM_WIN[battle.severity]

        return Outcome(
            description,
            score_change,
            _DAYS_PASSED_DICE_TABLE[battle.severity].roll(),
            did_flip_initiative,
            battle_change=battle,
        )
