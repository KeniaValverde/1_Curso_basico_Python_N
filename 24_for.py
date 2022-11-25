'''
for element in range(1,21):
    print(element)
'''

my_list = [21, 43, 89, 63]
for element in  my_list:
    print(element)

my_tuple = ('hola', 'camino', 'caminar')
for element in my_tuple:
    print(element)

product = {
    'name':'camisa',
    'price':100,
    'stock':89
}

for key in product:
    print(key, '=>', product[key])

for key, value in product.items():
    print(key, '=>, value')


#Lista de diccionario
people = [
    {
        'name':'nico',
        'age':34
    },
    {
        'name':'zule',
        'age':45
    },
    {
        'name':'santi',
        'age':4
    }
]

for person in people:
    print(person['name'])

for person in people:
    print('name=>',person['name'])