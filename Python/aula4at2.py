cont = 1
soma = 0
print('\tInforme a nota de 10 alunos')

while cont <= 10:
    nota = float(input(f'Digite a  {i + 1}° nota: '))
    soma += nota
    cont += 1
media = soma / 10

print(f'A media de nota dos alunos é {media}')
