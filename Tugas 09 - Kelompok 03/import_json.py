import sqlite3
import json

DATABASE = "seat.db"

def import_json():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    with open("seat_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # ==========================
    # Hapus data lama
    # ==========================
    cursor.execute("DELETE FROM emotion_analysis")
    cursor.execute("DELETE FROM emotion_check")
    cursor.execute("DELETE FROM focus_timer")
    cursor.execute("DELETE FROM activity")
    cursor.execute("DELETE FROM user")

    # ==========================
    # USER
    # ==========================
    for user in data["user"]:

        cursor.execute("""
        INSERT INTO user(id_user, nama)
        VALUES(?, ?)
        """, (
            user["id_user"],
            user["nama"]
        ))

    # ==========================
    # EMOTION CHECK
    # ==========================
    for check in data["emotion_check"]:

        cursor.execute("""
        INSERT INTO emotion_check
        (id_check, id_user, emosi, tanggal)
        VALUES (?, ?, ?, ?)
        """, (
            check["id_check"],
            check["id_user"],
            check["emosi"],
            check["tanggal"]
        ))

    # ==========================
    # EMOTION ANALYSIS
    # ==========================
    for analysis in data["emotion_analysis"]:

        cursor.execute("""
        INSERT INTO emotion_analysis
        (id_analysis, id_check, stress, insight, saran)
        VALUES (?, ?, ?, ?, ?)
        """, (
            analysis["id_analysis"],
            analysis["id_check"],
            analysis["stress"],
            analysis["insight"],
            analysis["saran"]
        ))

    # ==========================
    # ACTIVITY
    # ==========================
    for activity in data["activity"]:

        cursor.execute("""
        INSERT INTO activity
        (id_activity, nama, status, tanggal)
        VALUES (?, ?, ?, ?)
        """, (
            activity["id_activity"],
            activity["nama"],
            activity["status"],
            activity["tanggal"]
        ))

    # ==========================
    # FOCUS TIMER
    # ==========================
    for timer in data["focus_timer"]:

        cursor.execute("""
        INSERT INTO focus_timer
        (id_timer, tingkat_stress, durasi_fokus, durasi_istirahat)
        VALUES (?, ?, ?, ?)
        """, (
            timer["id_timer"],
            timer["tingkat_stress"],
            timer["durasi_fokus"],
            timer["durasi_istirahat"]
        ))

    conn.commit()
    conn.close()

    print("\n✅ Semua data berhasil diimport dari seat_data.json")