from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def ensure_complaint_columns():
    with db.engine.connect() as conn:
        table_exists = conn.execute(
            text("SELECT name FROM sqlite_master WHERE type='table' AND name='complaints'")
        ).scalar()

        if not table_exists:
            return

        existing_columns = {
            row[1]
            for row in conn.execute(text("PRAGMA table_info(complaints)"))
        }

        if "sentiment" not in existing_columns:
            conn.execute(text("ALTER TABLE complaints ADD COLUMN sentiment VARCHAR(20)"))
