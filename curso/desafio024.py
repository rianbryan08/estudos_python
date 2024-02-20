from random import randint
from time import sleep

pc = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número, entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

player =  int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

sleep(2)

if player == pc:
    print('Parabéns, você acertou')

else:
    quit('Você perdeu')