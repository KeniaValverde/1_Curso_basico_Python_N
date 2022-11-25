person = {
    'name' : 'nico',
    'last_name' : 'molina',
    'langs' : ['python','javascript'],
    'age' : 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
#agregar in datoi en langs
person['langs'].append('rust')
print(person)

#eliminar datos en un diccionario
del person['last_name']
#con pop hay que especificar el dato que se quiere eliminar
#person.pop()

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())