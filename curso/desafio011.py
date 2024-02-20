largura = float(input('Digite a largura de sua parede: '))
altura = float(input('Digite a altura de sua parede: '))

area = largura * altura

print('A área da parede é {:.2f} metros quadrado'.format(area))

tinta = area / 2

print('Vai precisar de {:.2f}l de tinta para pintar sua parede'.format(tinta))