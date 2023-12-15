kdmk = ['Mk01', 'Mk02', 'Mk03', 'Mk04', 'Mk05']
nama_mk = ['Jarkom', 'Algoritma', 'Sistem Operasi', 'kalkulus', 'PTI']
sks = [2, 4, 3, 2, 3]
print('========================Awal======================')
print('kode         Mata Kuliah         Sks')
print(kdmk[0], '       ', nama_mk[0], '             ', sks[0])
print(kdmk[1], '       ', nama_mk[1], '          ', sks[1])
print(kdmk[2], '       ', nama_mk[2], '     ', sks[2])
print(kdmk[3], '       ', nama_mk[3], '           ', sks[3])
print(kdmk[4], '       ', nama_mk[4], '                ', sks[4])

print()
kdmk_list = kdmk + sks
print('================menggabungkan kdmk dan sks ======')
print(kdmk_list)


print('kode         Mata Kuliah         Sks')
print(kdmk[0], '       ', nama_mk[0], '             ', sks[0])
print(kdmk[1], '       ', nama_mk[1], '          ', sks[1])
print(kdmk[2], '       ', nama_mk[2], '     ', sks[2])

print()

kodmk = ['Mk01', 'Mk02', 'Mk03']
nama_mkl = ['Jarkom', 'Algoritma', 'Sistem Operasi']
sks = [2, 4, 3]
print('=======================hapus=====================')
print('kode         Mata Kuliah         Sks')
print(kdmk[0], '       ', nama_mk[0], '             ', sks[0])
print(kdmk[1], '       ', nama_mk[1], '          ', sks[1])
print(kdmk[2], '       ', nama_mk[2], '     ', sks[2])
sks.remove(4)
print(sks)

print()
print('======================slicing====================')
Sks_list=[2, 4, 3, 2, 3]
sks_=Sks_list[1:3]
print(sks_)



print()
print('=======================in operator==================')
print(3 in Sks_list)
print(7 in Sks_list)
print(2 not in Sks_list)
print(7 not in Sks_list)