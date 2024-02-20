letra = input('Digite qualquer letra: ')

if letra in ['a', 'e', 'i', 'o', 'u']:
    print('A letra {} é uma vogal'.format(letra))

else:
    quit('A letra {} é uma consoante'.format(letra))