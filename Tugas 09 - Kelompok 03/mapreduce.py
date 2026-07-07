import os
import json
from collections import defaultdict

# ======================================================
# MEMBACA FILE JSON
# ======================================================

BASE_DIR = os.path.dirname(__file__)
json_path = os.path.join(BASE_DIR, "emotion_big.json")

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

analisis = data["emotion_analysis"]

print("=" * 50)
print("📊 PENGOLAHAN DATA EMOSI DENGAN MAPREDUCE")
print("=" * 50)

# ======================================================
# MAP
# Mengubah setiap data menjadi pasangan (stress, 1)
# ======================================================

mapped = []

for item in analisis:
    mapped.append((item["stress"], 1))

print("\n[1] MAP")
print("-" * 50)
print("10 data pertama hasil mapping:")
print(mapped[:10])

# ======================================================
# SHUFFLE
# Mengelompokkan data berdasarkan tingkat stress
# ======================================================

grouped = defaultdict(list)

for key, value in mapped:
    grouped[key].append(value)

print("\n[2] SHUFFLE")
print("-" * 50)

for key, values in grouped.items():
    print(f"{key:<8}: {len(values)} data")

# ======================================================
# FILTER
# Mengambil hanya stress Sedang dan Tinggi
# ======================================================

filtered = {}

for key, values in grouped.items():
    if key in ["Sedang", "Tinggi"]:
        filtered[key] = values

print("\n[3] FILTER")
print("-" * 50)
print("Kategori yang diproses:")

for key in filtered:
    print(f"- {key}")

# ======================================================
# REDUCE
# Menjumlahkan seluruh data pada tiap kategori
# ======================================================

reduced = {}

for key, values in filtered.items():
    reduced[key] = sum(values)

print("\n[4] REDUCE")
print("-" * 50)

for key, total in reduced.items():
    print(f"Jumlah pengguna dengan stress {key:<7}: {total}")

print("-" * 50)
print(f"Total data emotion_analysis : {len(analisis)}")
print("=" * 50)