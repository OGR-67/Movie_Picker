import sqlite3
from paths import DB_PATH


DB_CONNECT = sqlite3.connect(DB_PATH)
