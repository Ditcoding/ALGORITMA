ulang = 'Y'
phi = 22/7

while ulang == 'Y':
    print("Menghitung Luas Lingkaran")
    print("Pilih menu untuk menghitung ")
    print('1. menggunakan diameter')
    print('2. menggunakan rusuk')

    pilih = int(input("pilih menu untuk menghitung : "))
                    
    ulang = input("Apakah anda ingin mengulang menginput data? Y/N : ")

    if ulang == 'N':
        if pilih == 1:
            d = int(input("Masukan Diameter : "))
            

            print("Luas lingkaran adalah", phi * d)
        else:
            if pilih == 2:
                r = int(input("Masukan Rusuk : "))
                print("Luas lingkaran adalah:", phi * (r*r))
            else:
                print("Maaf menu yang anda pilih tidak tersedia")