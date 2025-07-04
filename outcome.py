from dataclasses import dataclass
from typing import Optional

from battle import Battle


@dataclass
class Outcome:
    description: str
    score_change: int
    days_passed: int
    did_initiative_change: bool
    battle_change: Optional[Battle] = None
