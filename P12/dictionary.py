person = {'Name' : 'David', 'Age' : 26, 'Weight': 82}
person['Job'] = 'Data science' #add item
print(person)
person['Age'] = 27 #modif item
print(person)
del person['Age'] #delete item
print(person)
person['Hobi'] = 'Mancing'
print(person)
print(len(person))

#lanjutan
print()
print()
for str1,num,in Mahasiswa1.items():
    print(str1, ':', num)
print()
print()
print(Mahasiswa1.keys())
print()
print()
print(Mahasiswa1.values())