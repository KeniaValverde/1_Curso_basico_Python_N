#and : los dos statements deben de cumplirse para ser verdadero
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and False =>', False and False)
print('False and True =>', False and True)

print(10>5 and 5<10)

stock = input('Ingrese el numeo de stock => ')
stock = int(stock)

print(stock >= 100 and stock <=1000)


#or : se cumple si una de las condiciones es verdadera
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or False =>', False or False)
print('False or True =>', False or True)

role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')