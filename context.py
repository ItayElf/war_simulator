from dataclasses import dataclass, field


@dataclass
class Context:
    side_a: str
    side_b: str
    score: int = 0

    initiative_at_side_a: bool = field(kw_only=True, default=True)
