i = 1
maior = 0

print('\tInforme 5 numeros\n')
while i <= 5:
    n = int(input('Digite o '+str(i)+'° numero: '))
    i += 1
    if n > maior:
        maior = n
    
print(f'O maior numero é: {maior}')