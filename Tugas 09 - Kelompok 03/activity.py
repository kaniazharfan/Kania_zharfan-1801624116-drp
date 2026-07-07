import sqlite3
from datetime import datetime

DATABASE = "seat.db"

def connect_db():
    return sqlite3.connect(DATABASE)


def tampilkan_activity():

    while True:

        print("\n" + "=" * 45)
        print("📋 TO-DO ACTIVITY 📋")
        print("=" * 45)
        print("1. Tambah Aktivitas")
        print("2. Lihat Aktivitas")
        print("3. Update Aktivitas")
        print("4. Hapus Aktivitas")
        print("5. Kembali ke Menu Fitur")

        pilihan = input("\n👉 Pilih menu (1-5): ")

        # ==========================
        # CREATE
        # ==========================
        if pilihan == "1":

            jumlah = int(input("\n📝 Berapa aktivitas yang ingin ditambahkan? "))

            conn = connect_db()
            cursor = conn.cursor()

            for i in range(jumlah):

                print(f"\nAktivitas ke-{i+1}")

                nama = input("Nama aktivitas : ")
                status = input("Status (Selesai/Belum Selesai): ")

                tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

                cursor.execute("""
                    INSERT INTO activity(nama, status, tanggal)
                    VALUES (?, ?, ?)
                """, (nama, status, tanggal))

            conn.commit()
            conn.close()

            print("\n✅ Aktivitas berhasil ditambahkan!")

        # ==========================
        # READ
        # ==========================
        elif pilihan == "2":

            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM activity")
            daftar_aktivitas = cursor.fetchall()

            conn.close()

            if len(daftar_aktivitas) == 0:

                print("\nBelum ada aktivitas ☹️.")

            else:

                print("\n" + "=" * 40)
                print("📋 DAFTAR AKTIVITAS")
                print("=" * 40)

                selesai = 0

                for aktivitas in daftar_aktivitas:

                    print(f"\nID      : {aktivitas[0]}")
                    print(f"Nama    : {aktivitas[1]}")
                    print(f"Status  : {aktivitas[2]}")
                    print(f"Tanggal : {aktivitas[3]}")

                    if aktivitas[2].lower() == "selesai":
                        selesai += 1

                total = len(daftar_aktivitas)
                belum = total - selesai
                persentase = (selesai / total) * 100

                print("\n" + "=" * 40)
                print("📖 RINGKASAN AKTIVITAS 📖")
                print("=" * 40)

                print(f"🌻 Total Aktivitas         : {total}")
                print(f"✅ Aktivitas Selesai       : {selesai}")
                print(f"❌ Aktivitas Belum Selesai : {belum}")
                print(f"📊 Persentase Selesai      : {persentase:.1f}%")

        # ==========================
        # UPDATE
        # ==========================
        elif pilihan == "3":

            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM activity")
            data = cursor.fetchall()

            if len(data) == 0:

                print("\nBelum ada aktivitas ☹️.")

            else:

                print("\n✨ Daftar Aktivitas ✨")

                for aktivitas in data:
                    print(f"{aktivitas[0]}. {aktivitas[1]}")

                id_activity = int(input("\nMasukkan ID aktivitas yang ingin diubah: "))

                nama_baru = input("Nama aktivitas baru : ")
                status_baru = input("Status baru (Selesai/Belum Selesai): ")

                cursor.execute("""
                    UPDATE activity
                    SET nama=?, status=?
                    WHERE id_activity=?
                """, (nama_baru, status_baru, id_activity))

                conn.commit()

                print("\n✅ Aktivitas berhasil diperbarui!")

            conn.close()

        # ==========================
        # DELETE
        # ==========================
        elif pilihan == "4":

            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM activity")
            data = cursor.fetchall()

            if len(data) == 0:

                print("\nBelum ada aktivitas ☹️.")

            else:

                print("\n📋 Daftar Aktivitas")

                for aktivitas in data:
                    print(f"{aktivitas[0]}. {aktivitas[1]}")

                id_activity = int(input("\nMasukkan ID aktivitas yang ingin dihapus: "))

                cursor.execute("""
                    DELETE FROM activity
                    WHERE id_activity=?
                """, (id_activity,))

                conn.commit()

                print("\n🗑️ Aktivitas berhasil dihapus!")

            conn.close()

        # ==========================
        # KEMBALI
        # ==========================
        elif pilihan == "5":

            break

        else:

            print("\n❌ Pilihan tidak tersedia!")

        input("\nTekan Enter untuk melanjutkan...")