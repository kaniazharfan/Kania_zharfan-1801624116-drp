import sqlite3

DATABASE = "seat.db"

def connect_db():
    return sqlite3.connect(DATABASE)


def tampilkan_waktu(tingkat_stres):

    print("\n🕰️ FOCUS TIMER")
    print("=" * 45)

    if tingkat_stres is None:

        print("⚠️ Anda belum melakukan Emotional Analytics.")
        print("Silakan lakukan analisis emosi terlebih dahulu.")

        input("\nTekan Enter untuk kembali...")
        return

    # ==========================
    # Menentukan durasi
    # ==========================

    if tingkat_stres == "rendah":

        durasi_fokus = 50
        durasi_istirahat = 10

    elif tingkat_stres == "sedang":

        durasi_fokus = 30
        durasi_istirahat = 5

    elif tingkat_stres == "tinggi":

        durasi_fokus = 20
        durasi_istirahat = 10

    # ==========================
    # Simpan ke database
    # ==========================

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO focus_timer
    (tingkat_stress, durasi_fokus, durasi_istirahat)

    VALUES (?, ?, ?)
    """, (
        tingkat_stres,
        durasi_fokus,
        durasi_istirahat
    ))

    conn.commit()
    conn.close()

    # ==========================
    # Tampilkan ke user
    # ==========================

    print(f"📊 Tingkat Stres : {tingkat_stres.capitalize()}")

    print("\n✅ Rekomendasi Timer")

    print(f"📚 Fokus      : {durasi_fokus} menit")
    print(f"☕ Istirahat  : {durasi_istirahat} menit")

    input("\nTekan Enter untuk kembali ke menu fitur...")