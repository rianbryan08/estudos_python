print('\tTurnos')
print('M - Matutino\nV - Vespertino\nN - Noturno\n')
turno = str(input('Digite o turno que você estuda: '))

if turno == 'M':
    print('Bom dia!')

elif turno == 'V':
    print('Boa tarde!')

elif turno == 'N':
    print('Boa noite!')

else:
    quit('Opção invalida')