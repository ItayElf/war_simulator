import random
from battle import Battle, BattleSeverity
from context import Context
from events.event import Event
from outcome import Outcome
from random_utils import choose_with_ranges

_BATTLE_SEVERITY_RANGES = {
    range(1, 4): BattleSeverity.SKIRMISH,
    range(4, 8): BattleSeverity.ENGAGEMENT,
    range(8, 10): BattleSeverity.CAMPAIGN,
    range(10, 11): BattleSeverity.DECISIVE_CLASH,
}


class BattleStartEvent(Event):
    def apply(self, context: Context) -> Outcome:
        severity = choose_with_ranges(_BATTLE_SEVERITY_RANGES)
        battle = Battle(self._generate_battle_name(), 0, severity, context.days_passed)
        initiator = context.side_a if context.initiative_at_side_a else context.side_b
        article = "an" if severity.value[0].lower() in "aeiou" else "a"

        return Outcome(
            f"{initiator} started {article} {severity.value} named {battle.name!r}",
            score_change=0,
            days_passed=0,
            did_initiative_change=False,
            battle_change=battle,
        )

    @staticmethod
    def _generate_battle_name():
        """
        Generates placeholder battle names
        """

        prefixes = ["Battle", "Siege", "Skirmish", "Conflict", "Clash", "War"]
        connectors = ["of", "at", "for"]
        places = [
            "Red Hill",
            "Eldergate",
            "Stonebridge",
            "Black Hollow",
            "Silver Marsh",
            "Iron Pass",
            "Thornwatch",
            "Daggerfall",
            "Sunspire",
            "Frostmoor",
            "Ashen Vale",
            "Grim Hollow",
            "Stormhaven",
            "Darkfen",
            "Rivercross",
        ]
        return f"{random.choice(prefixes)} {random.choice(connectors)} {random.choice(places)}"
