cont = 1
total = 0
valor = 0

while cont < 5:
    valor = int(input('Digite o '+str(cont)+' valor: '))
    cont += 1

    while valor < 0:
        valor = int(input('Valores negativos não são aceitos.' + 'Digite um novo valor para o '+str(cont)+' Valor: '))

        total += valor

print('Resultado da soma = {}'.format(total))