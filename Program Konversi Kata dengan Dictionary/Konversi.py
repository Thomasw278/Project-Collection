print("=" * 73)
print("========== Program Konversi Kata dengan Menggunakan Dictionary ==========")
print("=" * 73)
Kunci = {"a": 0, "b" : 1, "c" : 2, "d" : 3,
         "e" : 4, "f" : 5, "g" : 6, "h" : 7,
         "i" : 8, "j" : 9, "k" : 10, "l" : 11,
         "m" : 12, "n" : 13, "o" : 14, "p" : 15,
         "q" : 16, "r" : 17, "s" : 18, "t" : 19,
         "u" : 20, "v" : 21, "w" : 22, "x" : 23,
         "y" : 24, "z" : 25} #Untuk mengambil value dari kunci yang diinputkan
Text = {}
for keys,values in Kunci.items():
    Text[values] = keys #Untuk Membalik Keadaan di Dictionary Kunci yang dimana sekarang Keys nya adalah Value dari Dictionary Kunci  
Acuan = True
while True:
    Plain = input("Masukkan Input Plain Text: ").lower().strip()
    Keyword = input("Masukkan Input Keyword Text: ").lower().strip()
    try:
        Plain1 = str(Plain)
        Keyword1 = str(Keyword)
        TampungPlain = []
        TampungKeyword = []
        for i in Plain1:
            TampungPlain.append(Kunci[i])
        for i in Keyword1:
            TampungKeyword.append(Kunci[i])
        TotalKeyword = sum(TampungKeyword)
        Final = []
        for i in TampungPlain:
            Final.append((i + TotalKeyword) % 26)
        Chipertext = []
        for i in Final:
            Chipertext.append(Text[i])
        Chipertext = "".join(Chipertext)
        print(f"Chipertext : {Chipertext}")
        Exit = input("Exit? (Ya / Tidak) : ").lower()
        if Exit == "ya":
            print("========== Terimakasih Telah Menggunakan Program Konversi Kata ==========")
            break
        elif Exit == "tidak":
            continue
        else:
            print("Pilihan Hanya Ya / Tidak")
            print("Maaf Program Harus Berhenti karena ada kesalah pahaman antara inputanmu")
            break
    except:
        print("Input Harus Berupa String")