from dataclasses import dataclass


@dataclass
class Outcome:
    description: str
    score_change: int
    days_passed: int
    did_initiative_change: bool
