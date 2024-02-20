from random import randint
pc = randint(0, 10)

print('Sou seu PC... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar?')

acertou = False
palpite = 0

while not acertou:
    jg = int(input('Qual é seu palpite '))
    palpite += 1
    
    if jg == pc:
        acertou = True

    else: 
        if jg < pc:
            print('Mais... Tente novamente. ')
        elif jg > pc:
                print('Menos... Tente novamente. ')
print(f'Acertou... com {palpite} tentativas. Parabéns')