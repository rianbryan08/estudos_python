n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 9 and media <= 10:
    conceito = 'A'

elif media >= 7.5 and media <= 9:
    conceito = 'B'

elif media >= 6 and media <= 7.5:
    conceito = 'C'

elif media >= 4 and media <= 6:
    conceito = 'D'

else:
    conceito = 'E'

print('\nSua primeira nota é: {} \nSua segunda nota é: {} \nSua média é: {} \nO seu conceito foi: {}'.format(n1, n2, media, conceito))

if conceito in ['A', 'B', 'C']:
    print('APROVADOR')

else:
    print('REPROVADO')
