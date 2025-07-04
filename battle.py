from dataclasses import dataclass
from enum import Enum


class BattleSeverity(Enum):
    SKIRMISH = "skirmish"
    ENGAGEMENT = "engagement"
    CAMPAIGN = "campaign"
    DECISIVE_CLASH = "decisive clash"


_BATTLE_SCORE_THRESHOLD = {
    BattleSeverity.SKIRMISH: 3,
    BattleSeverity.ENGAGEMENT: 6,
    BattleSeverity.CAMPAIGN: 10,
    BattleSeverity.DECISIVE_CLASH: 15,
}


@dataclass
class Battle:
    name: str
    score: int
    severity: BattleSeverity
    started_at: int  # After how many days did the battle started
    is_active: bool = True
