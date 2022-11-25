'''
while True:
    print('se ejecuto')


counter = 0

while counter < 10:
    counter += 1
    print(counter)

#termina el ciclo cuando llega a 15
counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
      break
    print(counter)

'''

#continue reinicia el ciclo

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
      continue
    print(counter)
