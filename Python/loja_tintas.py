import math

area = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

litros = area / 6 * 1.1

latas = math.ceil(litros / 18)

galoes = math.ceil(litros / 3.6)

preco_latas = latas * 80

preco_galoes = galoes * 25

latas_mistura = int(litros / 18)
resto = litros % 18
if resto > 0:
    galoes_mistura = math.ceil(resto / 3.6)
else:
    galoes_mistura = 0

preco_mistura = latas_mistura * 80 + galoes_mistura * 25

print("\nQuantidade de tinta necessária: {:.2f} litros".format(litros))
print("Comprar apenas latas de 18 litros: {} latas - R$ {:.2f}".format(latas, preco_latas))
print("Comprar apenas galões de 3.6 litros: {} galões - R$ {:.2f}".format(galoes, preco_galoes))
print("Misturar latas e galões: {} latas e {} galões - R$ {:.2f}".format(latas_mistura, galoes_mistura, preco_mistura))