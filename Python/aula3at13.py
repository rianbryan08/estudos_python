l1 = int(input('lado 1: '))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print('Não pode ser um triangulo')

elif l1 == l2 == l3:
    print('Equílatero')

elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Isósceles')

else:
    quit('Escaleno')