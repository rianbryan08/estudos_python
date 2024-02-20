from math import hypot

cat_op = float(input('Digite o valor do cateto oposto: '))
cat_ad = float(input('Digite ad valor do cateto adjacente: '))

hipotenusa = hypot(cat_ad, cat_op)

print('O valor do cateto oposto é {} e o adjacente é {}'.format(cat_op, cat_ad))
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))