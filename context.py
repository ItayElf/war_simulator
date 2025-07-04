from dataclasses import dataclass, field
from typing import List

from battle import Battle


@dataclass
class Context:
    side_a: str
    side_b: str
    score: int = 0

    days_passed: int = field(kw_only=True, default=0)
    initiative_at_side_a: bool = field(kw_only=True, default=True)
    battles: List[Battle] = field(init=False, default_factory=list)
