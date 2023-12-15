kdmk = ['Mk01', 'Mk02', 'Mk03']
nama_mk = ['Jarkom', 'Algoritma', 'Sistem Operasi']
sks = [2, 4, 3]
print(kdmk[0])
print(nama_mk[0])
print(sks[0])
print('================================================')
print('kode         Mata Kuliah         Sks')
print('================================================')
print(kdmk[0], '       ', nama_mk[0], '             ', sks[0])
print(kdmk[1], '       ', nama_mk[1], '          ', sks[1])
print(kdmk[2], '       ', nama_mk[2], '     ', sks[2])
print()
print(kdmk)

kdmk =['mk00', 'mk02', 'mk03']
print(id(kdmk))
print(kdmk)
print()
mk = 'mata kuliah '
print(mk)
print(id(mk))

#Menambahkan list
print()
list1 = ['a', 'b', 'c']
list2 = [1,2,3]
list1.extend('d')
print(list1)

print()
n_list = [11,22,33,44,55,66]
print(n_list)
del n_list[3]
print(n_list)
n_list.remove(55)
print(n_list)

print()
n_list =[10,20,30]
print(n_list) #print seluruh item
n = n_list.pop()
print('n =', n)
print('n_list = ', n_list)


