print("=" * 40)
print("===== Program Kalkulator Sederhana =====")
print("=" * 40)
Hasil = True
while True:
    print("""Operator Yang Tersedia :
          1. Penjumlahan
          2. Pengurangan
          3. Perkalian
          4. Pembagian
          Input Q untuk Keluar dari Program""")
    Operator = str(input("Masukkan Operator Yang Dipilih atau Masukkan Q untuk keluar dari program : ")).lower()
    Tampung = [] # Buat nampung hasil dari operasi yang tersedi
    if Operator == "1": #Buat Operasi Tambah
        Pilihan = int(input("Mau Melakukan Operasi Penjumlahan Berapa kali : "))
        for i in range(Pilihan):
            Angka = int(input(f"Masukkan Bilangan ke- {i + 1}: "))
            Tampung.append(Angka)
        Total = sum(Tampung)
        print(f"Jadi Hasil dari Operasi Penjumlahan dari {Pilihan} Bilangan adalah : {Total}")
        print()
    elif Operator == "2": #Buat Operasi Pengurangan
        Pilihan = int(input("Mau Melakukan Operasi Pengurangan Berapa kali : "))
        for i in range(Pilihan):
            Angka = int(input(f"Masukkan Bilangan ke- {i + 1}: "))
            Tampung.append(Angka)
        Pengurang = Tampung[0]
        for i in Tampung[1::]:
            Pengurang -= i
        print(f"Jadi Hasil dari Operasi Pengurangan dari {Pilihan} Bilangan adalah : {Pengurang}")
        print()
    elif Operator == "3": #Buat Operasi Perkalian
        Pilihan = int(input("Mau Melakukan Operasi Perkalian Berapa kali : "))
        for i in range(Pilihan):
            Angka = int(input(f"Masukkan Bilangan ke- {i + 1}: "))
            Tampung.append(Angka)
        Perkalian = Tampung[0]
        for i in Tampung[1::]:
            Perkalian *= i
        print(f"Jadi Hasil dari Operasi Perkalian dari {Pilihan} Bilangan adalah : {Perkalian}")
        print()
    elif Operator == "4": #Buat Operasi Pembagian
        Pilihan = int(input("Mau Melakukan Operasi Pembagian Berapa kali : "))
        for i in range(Pilihan):
            Angka = int(input(f"Masukkan Bilangan ke- {i + 1}: "))
            Tampung.append(Angka)
        Pembagi = Tampung[0]
        for i in Tampung[1::]:
            Pembagi /= i
        print(f"Jadi Hasil dari Operasi Pembagian dari {Pilihan} Bilangan adalah : {Pembagi}")
        print()
    elif Operator == "q": #Buat Keluar dari Progarm
        Hasil = False
        print("Terimakasih Telah Menggunakan Program Kalkulator Sederhana")
        break
    else: #Jika Terjadi Kesalahan dalam menginput bagian operator
        print("Pilihan Hanya Tersedia antara 1-4 / Q")
        print()
        continue