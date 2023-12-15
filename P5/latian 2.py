print("===================================================================")

print("Kami menjual minuman isi 6 kaleng @0.355 Liter")
print("kami juga menjual minuman nonpaket 1 kaleng @2 Liter")
print("1.Paket")
print("2.Nonpaket")
print("===================================================================")
pilihan = str(input("Pilih [1/2] = "))

if pilihan=="1":
    paket=6*0.355
    print("Jumlah Literan Minuman Paket =", paket, "Liter")

else :
    if pilihan=="2":
        nonpaket=1*2
        print("Jumlah Literan Minuman Paket =",nonpaket, "Liter")
    else :
        print("Maaf Pilihan Anda Salah")