import sqlite3

DATABASE = "seat.db"

def connect_db():
    return sqlite3.connect(DATABASE)


def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    # ======================
    # USER
    # ======================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL
    )
    """)

    # ======================
    # EMOTION CHECK
    # ======================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emotion_check(
        id_check INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        emosi TEXT,
        tanggal TEXT
    )
    """)

    # ======================
    # EMOTION ANALYSIS
    # ======================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emotion_analysis(
        id_analysis INTEGER PRIMARY KEY AUTOINCREMENT,
        id_check INTEGER,
        stress TEXT,
        insight TEXT,
        saran TEXT
    )
    """)

    # ======================
    # ACTIVITY
    # ======================
    cursor.execute("""
CREATE TABLE IF NOT EXISTS activity(
    id_activity INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    status TEXT,
    tanggal TEXT
)
""")

    # ======================
    # FOCUS TIMER
    # ======================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS focus_timer(
        id_timer INTEGER PRIMARY KEY AUTOINCREMENT,
        tingkat_stress TEXT,
        durasi_fokus INTEGER,
        durasi_istirahat INTEGER
    )
    """)

    conn.commit()
    conn.close()