from context import Context
from outcome import Outcome


class EngineLogger:
    def __init__(self, context: Context) -> None:
        self.context = context

    def log_outcome(self, outcome: Outcome):
        initiative_text = ", flipping the initiative" if outcome.did_initiative_change else ""
        self.log(f"{outcome.description}{initiative_text}")

    def log(self, message: str):
        print(
            f"[{'*' if self.context.initiative_at_side_a else ''}{self.context.side_a}]"
            f"[{self.context.score:+d}]"
            f"[{'*' if not self.context.initiative_at_side_a else ''}{self.context.side_b}]"
            f"[{self.context.days_passed}D]"
            f" {message}"
        )
