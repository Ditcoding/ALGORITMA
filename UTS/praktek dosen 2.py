print("Selamat berbelanja di toko bahagia selalu...")
isi = str(input("Mau isi data [Y = Steuju] = "))
if isi == "Y":
    kode_barang = str(input("Kode Barang     : "))
    nama_barang = str(input("Nama Barang     : "))
    harga_satuan = int(input("Harga satuan   : "))
    stok_barang = int(input("Stok barang     : "))
    jumlah_jual = int(input("Jumlah jual     : "))
    harga_jual = jumlah_jual * harga_satuan
    total_harga = 0
    total_harga = total_harga + harga_jual
    stok_barang = stok_barang - jumlah_jual
    print()
    print("===========================================")
    print(".:: Cetak Jurnal Penjuualan")
    print("===========================================")
    print("Kode barang      : ", kode_barang)
    print("Nama Barang      : ", nama_barang)
    print("Harga Jual       : ", harga_jual)
    print("Jumlah jual      : ", jumlah_jual)
    print("===========================================")
    print("harga Jual       : ", harga_jual)
    print("Total Harga      : ", total_harga)
    print("===========================================")
    print("Sisa Stok = ", stok_barang)
else:
    print("terimakasih telah mengisi data")