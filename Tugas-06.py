import datetime

# Tanya kegiatan
kegiatan = input("Apa kegiatan yang akan Anda lakukan? (sarapan / berangkat kerja): ").strip().lower()

if kegiatan == "sarapan":
    # Tanya menu
    menu = input("Menu sarapan apa yang Anda inginkan? ").strip().lower()
    if menu == "telur" or menu == "ikan" or menu == "nugget":
        print(f"Anda memilih {menu}. Bahan sudah tersedia, silakan masak terlebih dahulu.")
    else:
        print(f"Anda memilih {menu}. Bahan tidak tersedia, Anda perlu membeli bahannya dulu.")

elif kegiatan == "berangkat kerja":
    # Cek waktu sekarang
    waktu_sekarang = datetime.datetime.now()
    jam_masuk_kerja = waktu_sekarang.replace(hour=8, minute=0, second=0, microsecond=0)
    if waktu_sekarang < jam_masuk_kerja:
        print(f"Sekarang jam {waktu_sekarang.strftime('%H:%M')}. Anda belum terlambat. Jam masuk 08:00.")
    else:
        print(f"Sekarang jam {waktu_sekarang.strftime('%H:%M')}. Anda sudah terlambat! Jam masuk 08:00.")

else:
    # Kalau user mengetik selain "sarapan" atau "berangkatkerja"
    print("Input tidak dikenali. Silakan ketik 'sarapan' atau 'berangkat kerja'.")