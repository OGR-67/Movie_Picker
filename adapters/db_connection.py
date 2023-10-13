import sqlite3
import threading
from paths import DB_PATH


def get_db() -> sqlite3.Connection:
    local_db = sqlite3.connect(DB_PATH)
    # Enable foreign key for sqlite3
    local_db.execute("PRAGMA foreign_keys=ON")
    return local_db


local = threading.local()


def get_thread_db() -> sqlite3.Connection:
    if not hasattr(local, "db"):
        local.db = get_db()
    return local.db  # type: ignore
