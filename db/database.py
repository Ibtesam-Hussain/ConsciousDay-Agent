import sqlite3

DB_NAME = "entries.db"

# ------------------ INIT ------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Entries table with username
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            journal TEXT,
            intention TEXT,
            dream TEXT,
            priorities TEXT,
            reflection TEXT,
            strategy TEXT,
            username TEXT
        )
    ''')

    conn.commit()
    conn.close()

# ------------------ AUTH ------------------
def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

# ------------------ ENTRIES ------------------
def save_entry(date, journal, intention, dream, priorities, reflection, strategy, username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy, username)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (date, journal, intention, dream, priorities, reflection, strategy, username))
    conn.commit()
    conn.close()

def get_entries_by_date(date_prefix, username):
    conn = sqlite3.connect('entries.db')
    c = conn.cursor()
    
    c.execute(
        "SELECT * FROM entries WHERE date LIKE ? AND username = ? ORDER BY date ASC",
        (f"{date_prefix}%", username)
    )
    return c.fetchall()

