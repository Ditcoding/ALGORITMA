ulang = 'Y'
phi = 22/7

while ulang =='Y' :
    rusuk = int(input("Masukan Rusuk Lingkaran = "))

    luas = phi * (rusuk*rusuk)
    
    ulang = input("Apakah anda ingin mengubah rusuk (Y/N) = ")          
    if ulang =='N':

        print("Luas lingkaran adalah", luas)
        print("Terimakasih")


