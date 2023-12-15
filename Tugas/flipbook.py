def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

def hitung_keliling(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling

panjang = int(input("Masukkan panjang persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))

pilihan_luas = input("Hitung luas? (ya/tidak): ").lower()

if pilihan_luas == 'ya':
    luas = hitung_luas(panjang, lebar)
    print("Luas persegi panjang:", luas)
else:
    pilihan_keliling = input("Hitung keliling? (ya/tidak): ").lower()
    if pilihan_keliling == 'ya':
        keliling = hitung_keliling(panjang, lebar)
        print("Keliling persegi panjang:", keliling)
    else:
        luas = hitung_luas(panjang, lebar)
        keliling = hitung_keliling(panjang, lebar)
        print("Luas persegi panjang:", luas)
        print("Keliling persegi panjang:", keliling)
