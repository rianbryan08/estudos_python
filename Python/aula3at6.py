n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite outro numero:'))

if n1>n2 and n1>n3:
    print('O maior numero é {}'.format(n1))

elif n2>n1 and n2>n3:
    print('O numero maior foi {}'.format(n2))

else:
    quit('O numero maior foi {}'.format(n3))