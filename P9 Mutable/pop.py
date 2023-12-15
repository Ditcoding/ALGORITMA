kdmk = ['mk01','mk02','mk03']
nama_mk=["kalkulus","algoritma","jarkom"]
sks=[3,4,2]
print(kdmk[0])
print(nama_mk[0])
print(sks[0])
print(kdmk,"   /   ",nama_mk,"   /    ",sks)
print('---------------------------------')
print("kode    mata_kuliah     SKS")
print('---------------------------------')
print(kdmk[0],'     ',nama_mk[0],'     ',sks[0])
print(kdmk[1],'     ',nama_mk[1],'    ',sks[1])
print(kdmk[2],'     ',nama_mk[2],'       ',sks[2])

print()
kdmk=["mk01","mk02","mk03"]
namamk=["kalkulus","algoritma","jarkom"]
sks=[3,4,2]
kdmk.append("mk04")
namamk.append("jarkom")
print("NAMBAH")
print(kdmk,"   /   ",namamk)
print("---------------------")
print("kode    mata kuliah     sks")
print("----------------------")
print(kdmk[0],"    ",namamk[0],"     ",sks[0])
print(kdmk[1],"    ",namamk[1],"    ",sks[1])
print(kdmk[2],"    ",namamk[2],"       ",sks[2])
print(kdmk[3],"    ",namamk[3],"       ",sks[2])

print()
print("HAPUS")
del kdmk[2]
del kdmk[0]
del namamk[2]
del namamk[0]
print(kdmk,"    /   ",namamk)

print()
print("SLICING")
kdmk=["mk01","mk02","mk03"]
namamk=["kalkulus","algoritma","jarkom"]
sks=[3,4,2]
print('---------------------------------')
print("kode    mata_kuliah     SKS")
print('---------------------------------')
print(kdmk[0],'     ',nama_mk[0],'     ',sks[0])
print(kdmk[1],'     ',nama_mk[1],'    ',sks[1])
print(kdmk[2],'     ',nama_mk[2],'       ',sks[2])

print()
print("IN/NOT IN")
kdmk=["mk01","mk02","mk03"]
nama_mk=["kalkulus","algoritma","jarkom"]
sks=[3,4,2]
print("mk01" in kdmk)
print("mk04" not in kdmk)