from context import Context
from engine.engine import Engine


def main():
    context = Context("Attacker", "Defender")
    engine = Engine(context)
    engine.simulate()


if __name__ == "__main__":
    main()
