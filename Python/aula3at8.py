valor1 = float(input('Digite o valor de um produto: '))
valor2 = float(input('Digite o valor de um produto: '))
valor3 = float(input('Digite o valor de um produto: '))

maior = valor1
menor = valor1

if valor2 > maior:
    maior = valor2

if valor3 > maior:
    maior = valor3

if valor2 < menor:
    menor = valor2

if valor3 < menor:
    menor = valor3

print('O prduto que você deve comprar é com esse valor por ser o mais barato {}.'.format(menor))