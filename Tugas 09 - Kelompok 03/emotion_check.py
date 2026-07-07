import sqlite3
from datetime import datetime

DATABASE = "seat.db"

def connect_db():
    return sqlite3.connect(DATABASE)

def cek_emosi(id_user):

    print("\n😊 CHECK-IN EMOSI HARI INI")
    print("=" * 45)

    print("1. 😄 Bahagia")
    print("2. 😌 Tenang")
    print("3. 😐 Biasa Saja")
    print("4. 😟 Cemas")
    print("5. 😔 Sedih")

    pilihan = input("\nPilih emosi (1-5): ")

    # Konversi angka menjadi nama emosi
    daftar_emosi = {
        "1": "Bahagia",
        "2": "Tenang",
        "3": "Biasa Saja",
        "4": "Cemas",
        "5": "Sedih"
    }

    emosi = daftar_emosi.get(pilihan)

    if emosi is None:
        print("\n❌ Pilihan tidak valid!")
        return None, None

    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emotion_check(id_user, emosi, tanggal)
    VALUES (?, ?, ?)
    """, (id_user, emosi, tanggal))

    conn.commit()

    id_check = cursor.lastrowid

    conn.close()

    return pilihan, id_check