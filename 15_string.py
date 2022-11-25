text = 'Ella sabe programar en Python'
print('Javascript' in text)
#si la palabra Python esta dentro del texto
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien!!')
else:
    print('Tambien elegiste bien')

size = len(text)
print(size)

#trasnformar el texto en mayusculas
print(text, text.upper())

#trasnformar el texto en minusculas
print(text, text.lower())

#contar cuantas veces hay x letra en el texto
print(text, text.count('a'))

#transforma el las letras mayusculas a minusculas y viceversa
print(text.swapcase())

#trasnformar el texto en minusculas
print(text.startswith('Ella'))

print(text.endswith('Rust'))

print(text.replace('Python', 'Go'))


print(text[0])

size = len(text)
print('size = ', size)
print(text[size-1])
print(text[-1])

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[10:26:2])
print(text[::2])