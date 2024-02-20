salario = float(input('Qual o seu salario? '))

aumento = salario * 0.15
salario_a = aumento + salario

print('Você possui um aumento de 15%')
print('Você tem um aumento de R${:.2f}'.format(aumento))
print('Você recebera R${:.2f}'.format(salario_a))