import random

user_option = input('Piedra, papel o tijera => ')
user_option = user_option.lower()
computer_option = ['piedra','papel','tijera']
computer_option2 = random.choice(computer_option)

if user_option == computer_option2:
    print('Empate!')
elif (user_option == 'piedra' and computer_option2 == 'tijera'):
    print('Piedra gana a tijera')
    print('user gano')
elif (user_option == 'tijera' and computer_option2 == 'papel'):
    print('Tijera gana a papel')
    print('user gano')
elif (user_option == 'papel' and computer_option2 == 'piedra'):
    print('Papel gana a piedra')
    print('user gano')
else:
    print(computer_option2 +' gana')
    print('Computer gano')