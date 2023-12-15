ulang = 'y'
total_harga = 0

while ulang == 'y':
    kode_barang = input("Masukan Kode Barang = ")
    nama_barang = input("Masukan Nama Barang = ")
    harga_satuan = float(input("Masukan Harga Satuan = "))
    stok_barang = input("Masukan Stok Barang = ")

    jumlah_barang_terjual = int(input("Masukan Jumlah barang terjual : "))

    harga_jual = harga_satuan*jumlah_barang_terjual
    total_harga += harga_jual
    
    print("Harga Jual Untuk ", nama_barang, "adalah", harga_jual)
    
    ulang = input("Apakah anda ngin mengulng data? (y/n) : " )

print("Terimakasih")