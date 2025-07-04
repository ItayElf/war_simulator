from dataclasses import dataclass
from enum import Enum


class BattleSeverity(Enum):
    SKIRMISH = "skirmish"
    ENGAGEMENT = "engagement"
    CAMPAIGN = "campaign"
    DECISIVE_CLASH = "decisive clash"


SCORE_INCREASE_FROM_WIN = {
    BattleSeverity.SKIRMISH: 5,
    BattleSeverity.ENGAGEMENT: 10,
    BattleSeverity.CAMPAIGN: 15,
    BattleSeverity.DECISIVE_CLASH: 20,
}


@dataclass
class Battle:
    name: str
    score: int
    severity: BattleSeverity
    started_at: int  # After how many days did the battle started
    is_active: bool = True
