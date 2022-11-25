my_dict = {}
print(type(my_dict))

my_dict = {
    'avion' : 'un avion es un vehiculo aereo',
    'name' : 'Kenia',
    'last_name' : 'Valverde Ramírez',
    'age' : '33'
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('unvalor'))

print('aviob' in my_dict)
print('otroqueno' in my_dict)

