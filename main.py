from context import Context
from engine.engine import Engine
from engine.engine_logger import EngineLogger
from engine.sql_engine_logger import SqlEngineLogger


def main():
    for _ in range(1000):
        context = Context("Attacker", "Defender")
        logger = SqlEngineLogger("database.db", context)
        engine = Engine(context, logger)

        logger.setup_tables()
        engine.simulate()


if __name__ == "__main__":
    main()
