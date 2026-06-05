from welcome import tampilkan_welcome
from tools import tampilkan_tools
from pilih_menu import pilih_menu

from emotion_preview import tampilkan_emotional_logic
from activity_preview import tampilkan_activity_logic
from focus_preview import tampilkan_focus_logic

user = tampilkan_welcome()

while True:

    menu = tampilkan_tools(user)

    if menu == "1":

        while True:

            fitur = pilih_menu()

            if fitur == "1":

                tampilkan_emotional_logic()

            elif fitur == "2":

                tampilkan_activity_logic()

            elif fitur == "3":

                tampilkan_focus_logic()

            elif fitur == "4":

                break

            else:

                print("\n❌ Pilihan tidak tersedia!")

    elif menu == "2":

        print("""
========================================
         TENTANG APLIKASI
========================================

Student Emotion Analytic Tool (SEAT)

Tujuan:
• Membantu mahasiswa mengenali kondisi emosi.
• Membantu mengelola aktivitas harian.
• Memberikan rekomendasi waktu fokus.
""")

        input("\nTekan Enter untuk kembali...")

    elif menu == "3":

        print(f"\n👋 Sampai jumpa, {user}!")
        print("Terima kasih telah menggunakan SEAT 🎀")
        break

    else:

        print("\n❌ Pilihan tidak tersedia!")