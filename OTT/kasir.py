ulang = 'Y'
while ulang == 'Y':
    print("""
    =============================
    Coffe Adit
    List Menu Coffe
    =============================
    a. Es Kopi Susu   : Rp 11.000
    b. Es Kopi Coklat : Rp 12.000
    c. Es Kopi Hitam  : Rp 11.000
    d. Es Capucino    : Rp 13.000
    =============================
    """)

    pesan = str(input("Masukan list abjad menu coffe = "))
    jumlahpesan = int(input("Masukan jumlah pesanan = "))
    if pesan == "a":
        listnama = "Es Kopi Susu"
        harga = int(11000*jumlahpesan)
        ppn = int(harga*0.1)
        if jumlahpesan >5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga=int(harga+ppn)

    elif pesan == "b":
        listnama = "Es Kopi Cokelat"
        harga = int(12000*jumlahpesan)
        ppn = int(harga*0.1)
        if jumlahpesan >5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga=int(harga+ppn)
    elif pesan == "c":
        listnama = "Es Kopi Hitam"
        harga = int(11000*jumlahpesan)
        ppn = int(harga*0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "d":
        listnama = "Es Capucino"
        harga = int(13000*jumlahpesan)
        ppn = int(harga*0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    else :
        listnama ="-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        ulang = input("Menu yang anda msukan tidak tersedia, apakah anda ingin mengulang pesanan? (Y/N) :" )
    print("=============================")
    print("Coffe Adit")
    print("=============================")
    print("Menu           = ", listnama)
    print("Jumlah Pesanan = ", jumlahpesan)
    print("Harga          = ", harga)
    print("Diskon         = ", diskon)
    print("PPN            = ", ppn)
    print("=============================")
    print("Jumlah Bayar   = ", totalharga)
    print("=============================")
    ulang = input("Apakah anda ingin pesan kembali (Y/N) : ")
    print("Terimakasih telah memesan menu kami.")

