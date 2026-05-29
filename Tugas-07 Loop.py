# soal 1 - papan catur

print("--- Layout Papan Catur 8x8 ---")
print()

for i in range(8): # loop untuk setiap baris (0 sampai 7)
    for j in range(8): # loop untuk setiap kolom dalam satu baris
        if (i + j) % 2 == 0: # kalau jumlah baris + kolom genap, cetak putih
            print("⬜", end="")
        else: # kalau ganjil, cetak hitam
            print("⬛", end="")
    print() # pindah baris setelah 8 kolom selesai

print()

# soal 2 - input aktivitas

print("--- Manajemen Aktivitas ---")
print()

list_akt = [] # list kosong untuk menyimpan semua aktivitas

while True: # terus minta input sampai user ketik 'done'
    akt = input("Nama aktivitas (ketik 'done' untuk selesai): ")

    if akt.lower() == 'done': # cek apakah user mau berhenti
        break

    ket = input("Keterangan: ") # input tambahan berupa keterangan aktivitas
    list_akt.append({'nama': akt, 'ket': ket}) # simpan sebagai dictionary ke dalam list

# tampilkan semua aktivitas yang sudah diinput
print()
print("--- Daftar Aktivitas ---")
print()

if len(list_akt) == 0: # kalau list kosong, kasih pesan
    print("Belum ada aktivitas yang dicatat.")
else:
    for i, data in enumerate(list_akt, start=1): # enumerate biar nomor mulai dari 1
        print(f"{i}. Aktivitas  : {data['nama']}")
        print(f"   Keterangan : {data['ket']}")
        print()

print(f"Total: {len(list_akt)} aktivitas tercatat.") # ringkasan jumlah aktivitas