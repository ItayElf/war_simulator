from context import Context
from outcome import Outcome


class EngineLogger:
    def __init__(self, context: Context) -> None:
        self.context = context

    def log_outcome(self, outcome: Outcome):
        initiative_text = ", flipping the initiative" if outcome.did_initiative_change else ""
        self.log(f"{outcome.description}{initiative_text}")

    def log_peace(self, outcome: str):
        winner = self.context.side_a if self.context.score > 0 else self.context.side_b
        article = "an" if outcome[0].lower() in "aeiou" else "a"
        self.log(f"{winner} won after {self.context.days_passed} days, securing {article} {outcome}")

    def log(self, message: str):
        active_battles = [b for b in self.context.battles if b.is_active]
        active_battles_text = f", {len(active_battles)}B" if active_battles else ""

        print(
            f"[{'*' if self.context.initiative_at_side_a else ''}{self.context.side_a}]"
            f"[{self.context.score:+d}]"
            f"[{'*' if not self.context.initiative_at_side_a else ''}{self.context.side_b}]"
            f"[{self.context.days_passed}D{active_battles_text}]"
            f" {message}"
        )
