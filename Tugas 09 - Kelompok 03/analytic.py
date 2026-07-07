import sqlite3

DATABASE = "seat.db"

def connect_db():
    return sqlite3.connect(DATABASE)


def tampilkan_analytics(id_check, pilihan):

    print("\n📊 HASIL ANALISIS EMOSI")
    print("=" * 45)

    tingkat_stres = ""
    insight = ""
    saran = ""

    if pilihan == "1":

        emosi = "😄 Bahagia"
        tingkat_stres = "Rendah"
        insight = "Kondisi emosional Anda sangat baik."
        saran = "Pertahankan rutinitas positif."

    elif pilihan == "2":

        emosi = "😌 Tenang"
        tingkat_stres = "Rendah"
        insight = "Anda mampu mengelola tekanan akademik."
        saran = "Tetap jaga keseimbangan belajar."

    elif pilihan == "3":

        emosi = "😐 Biasa Saja"
        tingkat_stres = "Sedang"
        insight = "Ada beberapa tekanan akademik."
        saran = "Susun prioritas tugas dengan baik."

    elif pilihan == "4":

        emosi = "😟 Cemas"
        tingkat_stres = "Tinggi"
        insight = "Deadline dan tugas meningkatkan kecemasan."
        saran = "Gunakan Focus Timer dan istirahat teratur."

    elif pilihan == "5":

        emosi = "😔 Sedih"
        tingkat_stres = "Tinggi"
        insight = "Anda mungkin mengalami kelelahan akademik."
        saran = "Luangkan waktu untuk self-care."

    else:

        print("Input tidak valid.")
        return None

    # ==========================
    # SIMPAN KE DATABASE
    # ==========================

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emotion_analysis
    (id_check, stress, insight, saran)

    VALUES (?, ?, ?, ?)
    """, (id_check, tingkat_stres, insight, saran))

    conn.commit()
    conn.close()

    # ==========================
    # TAMPILKAN HASIL
    # ==========================

    print(f"Emosi Dominan : {emosi}")
    print(f"Tingkat Stres : {tingkat_stres}")
    print(f"Insight       : {insight}")
    print(f"Saran         : {saran}")

    input("\nTekan Enter untuk kembali ke menu fitur...")

    return tingkat_stres.lower()