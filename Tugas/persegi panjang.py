print("Kita akan menghitung persegi panjang")

panjang = int(input("Masukkan panjang persegi panjang = "))
lebar = int(input("Masukkan lebar persegi panjang = "))

print("Pilih menu berikut :")
print("1. Hitung Luas")
print("2. Hitung Keliling")
print("3. Hitung luas dan keliling")

pilih_menu = int(input("Pilih menu (angka) = "))

if pilih_menu == 1:
    print("Luas persegi panjang adalah : ", panjang * lebar)
elif pilih_menu == 2:
    print("keliling persegi panjang adalah : ", 2 * (panjang + lebar))
elif pilih_menu == 3:
    print("Luas persegi panjang adalah : ", panjang * lebar)
    print("keliling persegi panjang adalah : ", 2 * (panjang + lebar)) 
else:
    print("Maaf menu yang anda msukan salah")       