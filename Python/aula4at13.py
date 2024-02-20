inicio = int(input('Digite um numero inicial: '))
fim = int(input('Digite um numero final: '))
soma = 0

while inicio <= fim:
    print(inicio)
    soma += inicio
    inicio += 1
print('A soma desses numeros: ',soma)
