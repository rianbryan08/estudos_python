soma = 0
media = 0
homem = 0
velho = 0
mulher = 0

for i in range(1, 5):
    print('----{} PESSOAS ----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    
    if i == 1 and sexo in 'Mm':
        homem = idade
        velho = nome
    
    if sexo in 'Mm' and idade > homem:
        homem = idade
        velho = nome
    
    if sexo in 'Ff' and idade < 20:
        mulher += 1

media = soma / 4
print(f'A media de idade do gp é de {media} anos')
print(f'O homem mais velho tem {homem} anos e se chama {velho}')
print(f'Ao todos são {mulher} mulheres com menos de 20 anos')
