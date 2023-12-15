#Pertama, kita harus menentukan seberapa banyak perulangannya yaitu sebanyak 7 kali. Kemudian variabel i berfungsi untuk menampung indeks dan fungsi range() berfungsi untuk membuat list dengan range dari 0-7, serta untuk merubah tipe data dari integer ke string kita menggunakan fungsi str(). Maka hasil dari perintah di atas seperti berikut.

ulang = 20
for i in range(ulang):
    print(f"Loop ke {i}")