import sqlite3
import threading
from paths import DB_PATH


def get_db() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


local = threading.local()


def get_thread_db() -> sqlite3.Connection:
    if not hasattr(local, "db"):
        local.db = get_db()
    return local.db  # type: ignore
