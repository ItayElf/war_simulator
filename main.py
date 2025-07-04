from context import Context
from engine.engine import Engine


def main():
    context = Context("Attacker", "Defender")
    engine = Engine(context)
    engine.progress_by_one_turn()


if __name__ == "__main__":
    main()
