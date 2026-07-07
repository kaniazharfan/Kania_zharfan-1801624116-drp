import sqlite3
import json

DATABASE = "seat.db"

def export_json():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    data = {}

    # ==========================
    # USER
    # ==========================
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()

    data["user"] = []

    for user in users:
        data["user"].append({
            "id_user": user[0],
            "nama": user[1]
        })

    # ==========================
    # EMOTION CHECK
    # ==========================
    cursor.execute("SELECT * FROM emotion_check")
    checks = cursor.fetchall()

    data["emotion_check"] = []

    for check in checks:
        data["emotion_check"].append({
            "id_check": check[0],
            "id_user": check[1],
            "emosi": check[2],
            "tanggal": check[3]
        })

    # ==========================
    # EMOTION ANALYSIS
    # ==========================
    cursor.execute("SELECT * FROM emotion_analysis")
    analyses = cursor.fetchall()

    data["emotion_analysis"] = []

    for analisis in analyses:
        data["emotion_analysis"].append({
            "id_analysis": analisis[0],
            "id_check": analisis[1],
            "stress": analisis[2],
            "insight": analisis[3],
            "saran": analisis[4]
        })

    # ==========================
    # ACTIVITY
    # ==========================
    cursor.execute("SELECT * FROM activity")
    activities = cursor.fetchall()

    data["activity"] = []

    for aktivitas in activities:
        data["activity"].append({
            "id_activity": aktivitas[0],
            "nama": aktivitas[1],
            "status": aktivitas[2],
            "tanggal": aktivitas[3]
        })

    # ==========================
    # FOCUS TIMER
    # ==========================
    cursor.execute("SELECT * FROM focus_timer")
    timers = cursor.fetchall()

    data["focus_timer"] = []

    for timer in timers:
        data["focus_timer"].append({
            "id_timer": timer[0],
            "tingkat_stress": timer[1],
            "durasi_fokus": timer[2],
            "durasi_istirahat": timer[3]
        })

    conn.close()

    with open("seat_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("\n✅ Semua data berhasil diexport ke seat_data.json")