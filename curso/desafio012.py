preco = float(input('Digite o valor do seu produto: '))

desconto = preco * 0.05
total = preco - desconto

print('O produto está com 5% de desconto')
print('O desconto foi de R${:.2f} e você pagara R${:.2f}'.format(desconto, total))