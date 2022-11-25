if True:
    print('debería ejecutarse')

if False:
    print('nunca se ejecuta')

#....

pet = input('¿Cual es tu mascota favorita?')

if pet == 'perro':
    print('genial tienes buen gusto')
if pet == 'gato':
    print('espero tengas suerte')
if pet == 'pez':
    print('eres lo máximo')
else:
    print('no tienes ninguna mascota interesante')


stock = int(input('Digita el stock =>'))

if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')