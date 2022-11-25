#NOt: al utilizar el not cambia el valor
#este se convierte en false
print(not True)
#y este se convierte en true
print(not False)

#and
print('Not And')
print(' Not True and True =>', not (True and True))
print('Not True and False =>', not (True and False))
print('Not False and False =>', not (False and False))
print('Not False and True =>', not (False and True))


role = input('Digita el rol => ')
print(not (role == 'admin' or role == 'seller'))