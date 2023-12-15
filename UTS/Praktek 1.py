ulangi = "y"

while ulangi == "y":
    nik = input("Masukkan NIK : ")
    nama = input("Masukkan Nama : ")
    usia = input("Masukkan Usia : ")
    gender = input("Masukkan Gender : ")
    alamat = input("Masukkan Alamat: ")
    hobi = input("Masukkan Hobi : ")

    print("\nData yang telah dimasukkan:")
    print("NIK :", nik)
    print("Nama :", nama)
    print("Usia :", usia)
    print("Gender :", gender)
    print("Alamat :", alamat)
    print("Hobi :", hobi)

    ulangi = input("\nApakah Anda ingin mengulang menginput data? (y/n): ")

print("Terima kasih! Program selesai.")
