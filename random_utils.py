from dataclasses import dataclass
import random
from typing import Dict, Optional, TypeVar

_T = TypeVar("_T")


@dataclass(frozen=True)
class Dice:
    sides: int
    times: int = 1
    modifier: int = 0

    def roll(self) -> int:
        total = sum(random.randint(1, self.sides) for _ in range(self.times))
        return total + self.modifier


def choose_with_ranges(ranges: Dict[range, _T], dice: Optional[Dice] = None) -> _T:
    if dice is None:
        dice = Dice(max(r.stop for r in ranges))

    result = dice.roll()
    for number_range in ranges:
        if result in number_range:
            return ranges[number_range]

    raise RuntimeError(f"Result {result} was not found in ranges: {ranges!r}")
