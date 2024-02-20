nome = str(input('Digite seu nome e sobrenome: ')).strip()

print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))

print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))