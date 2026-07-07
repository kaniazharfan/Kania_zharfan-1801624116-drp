from export_json import export_json
from import_json import import_json

def tampilkan_kelola_data():

    while True:

        print("\n" + "=" * 45)
        print("📂 KELOLA DATA")
        print("=" * 45)
        print("1. Export Data ke JSON")
        print("2. Import Data dari JSON")
        print("3. Kembali")

        pilihan = input("\n👉 Pilih menu (1-3): ")

        if pilihan == "1":

            export_json()

            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "2":

            import_json()

            input("\nTekan Enter untuk melanjutkan...")

        elif pilihan == "3":

            break

        else:

            print("\n❌ Pilihan tidak tersedia!")