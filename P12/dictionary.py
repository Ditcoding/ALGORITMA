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