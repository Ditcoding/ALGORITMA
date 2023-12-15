def luas_persegi(sisi):
    return sisi * sisi

#Tidak menghasilkan output!!
luas_persegi(10)

#Menghasilkan Output
print("Luas persegi dengan sisi 4 adalah:", luas_persegi(4))

#Bisa juga simpan di dalam variabel
persegi_besar = luas_persegi(100)
persegi_kecil = luas_persegi(50)
print("Total luas persegi besar dan kecil adalah:", persegi_besar + persegi_kecil)