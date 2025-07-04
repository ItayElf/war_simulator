from enum import Enum, auto

from random_utils import Dice


class Severity(Enum):
    MINOR = auto()
    MODERATE = auto()
    STRONG = auto()
    MAJOR = auto()
    TRANSFORMATIVE = auto()


SEVERITY_RANGES = {
    range(1, 4): Severity.MINOR,
    range(4, 7): Severity.MODERATE,
    range(7, 9): Severity.STRONG,
    range(9, 10): Severity.MAJOR,
    range(10, 11): Severity.TRANSFORMATIVE,
}

SEVERITY_SCORE = {
    Severity.MINOR: 1,
    Severity.MODERATE: 3,
    Severity.STRONG: 5,
    Severity.MAJOR: 10,
    Severity.TRANSFORMATIVE: 15,
}

SEVERITY_DAYS_DICE = {
    Severity.MINOR: Dice(10),
    Severity.MODERATE: Dice(10, modifier=2),
    Severity.STRONG: Dice(10, modifier=4),
    Severity.MAJOR: Dice(10, modifier=6),
    Severity.TRANSFORMATIVE: Dice(10, modifier=8),
}
