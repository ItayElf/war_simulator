from context import Context
from engine.engine import Engine


def main():
    context = Context("Attacker", "Defender")
    engine = Engine(context)
    engine.logger.log(engine.dispatch_event().description)


if __name__ == "__main__":
    main()
