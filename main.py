from context import Context
from engine.engine import Engine


def main():
    context = Context("Attacker", "Defender")
    engine = Engine(context)
    print(engine.dispatch_event())


if __name__ == "__main__":
    main()
