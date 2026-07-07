import sqlite3

DATABASE = "seat.db"

def tampilkan_statistik():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print("\n" + "="*45)
    print("📊 STATISTIK PENGGUNA")
    print("="*45)

    # ==========================
    # Total Check Emosi
    # ==========================

    cursor.execute("""
    SELECT COUNT(*)
    FROM emotion_check
    """)

    total_check = cursor.fetchone()[0]

    # ==========================
    # Stress Rendah
    # ==========================

    cursor.execute("""
    SELECT COUNT(*)
    FROM emotion_analysis
    WHERE stress='Rendah'
    """)

    rendah = cursor.fetchone()[0]

    # ==========================
    # Stress Sedang
    # ==========================

    cursor.execute("""
    SELECT COUNT(*)
    FROM emotion_analysis
    WHERE stress='Sedang'
    """)

    sedang = cursor.fetchone()[0]

    # ==========================
    # Stress Tinggi
    # ==========================

    cursor.execute("""
    SELECT COUNT(*)
    FROM emotion_analysis
    WHERE stress='Tinggi'
    """)

    tinggi = cursor.fetchone()[0]

    # ==========================
    # Emosi paling sering muncul
    # ==========================

    cursor.execute("""
    SELECT emosi, COUNT(*)
    FROM emotion_check
    GROUP BY emosi
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """)

    hasil = cursor.fetchone()

    if hasil:
        emosi = hasil[0]
        jumlah = hasil[1]
    else:
        emosi = "-"
        jumlah = 0

    # ==========================
    # Persentase aktivitas selesai
    # ==========================

    cursor.execute("""
    SELECT COUNT(*)
    FROM activity
    """)

    total_activity = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM activity
    WHERE LOWER(status)='selesai'
    """)

    selesai = cursor.fetchone()[0]

    if total_activity == 0:
        persentase = 0
    else:
        persentase = (selesai / total_activity) * 100

    # ==========================
    # Timer paling sering digunakan
    # ==========================

    cursor.execute("""
    SELECT durasi_fokus, COUNT(*)
    FROM focus_timer
    GROUP BY durasi_fokus
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """)

    timer = cursor.fetchone()

    if timer:
        fokus = timer[0]
    else:
        fokus = "-"

    print(f"📝 Total Check Emosi      : {total_check}")
    print(f"😊 Stress Rendah          : {rendah}")
    print(f"😐 Stress Sedang          : {sedang}")
    print(f"😟 Stress Tinggi          : {tinggi}")

    print()
    print(f"❤️ Emosi Terbanyak        : {emosi} ({jumlah} kali)")
    print(f"📋 Aktivitas Selesai      : {persentase:.1f}%")
    print(f"⏱️ Timer Favorit          : {fokus} menit")

    conn.close()

    input("\nTekan Enter untuk kembali...")