from context import Context


class EngineLogger:
    def __init__(self, context: Context) -> None:
        self.context = context

    def log(self, message: str):
        print(
            f"[{'*' if self.context.initiative_at_side_a else ''}{self.context.side_a}]"
            f"[{'*' if not self.context.initiative_at_side_a else ''}{self.context.score:+d}]"
            f"[{self.context.side_b}]"
            f"[{self.context.days_passed} days]"
            f" {message}"
        )
