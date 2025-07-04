import sqlite3

from context import Context
from outcome import Outcome


CREATE_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS context (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    war_id INTEGER NOT NULL, 
    side_a TEXT NOT NULL,
    side_b TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    days_passed INTEGER DEFAULT 0,
    initiative_at_side_a BOOLEAN DEFAULT 1
);
CREATE TABLE IF NOT EXISTS battles (
    battle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    context_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    score INTEGER NOT NULL,
    severity TEXT NOT NULL,
    started_at INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (context_id) REFERENCES context(id)
)
"""


class SqlEngineLogger:
    """
    A class that logs the engine to sqlite database.
    This class is mainly used for debugging.
    """

    def __init__(self, database_path: str, context: Context) -> None:
        self.conn = sqlite3.connect(database_path)
        self.context = context
        self.war_id = 0
        self.load_next_war_id()

    def setup_tables(self):
        self.conn.executescript(CREATE_TABLES_SQL)
        self.conn.commit()

    def log_outcome(self, outcome: Outcome):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO context (war_id, side_a, side_b, score, days_passed, initiative_at_side_a)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                self.war_id,
                self.context.side_a,
                self.context.side_b,
                self.context.score,
                self.context.days_passed,
                int(self.context.initiative_at_side_a),
            ),
        )
        context_id = cursor.lastrowid

        for battle in self.context.battles:
            cursor.execute(
                """
                INSERT INTO battles (context_id, name, score, severity, started_at, is_active)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    context_id,
                    battle.name,
                    battle.score,
                    battle.severity.value,
                    battle.started_at,
                    int(battle.is_active),
                ),
            )
        self.conn.commit()

    def log_peace(self, outcome: str):
        self.load_next_war_id()

    def load_next_war_id(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(war_id) FROM context")
            result = cursor.fetchone()[0]
            self.war_id = (result or 0) + 1
        except sqlite3.OperationalError:
            self.war_id = 0
