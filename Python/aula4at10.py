i = 1
soma = 0
print('\tInforme 5 numeros\n')
while i <= 5:
    n = int(input('Digite o '+str(i)+'° numero: '))
    i += 1
    soma += n
    media = soma / 5
print(f'A soma é {soma} e a media é {media}')
