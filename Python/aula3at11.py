print('\t DIAS DA SEMANA\n')
print('1 - DOMINGO\n2 - SEGUNDA\n3 - TERÇA\n4 - QUARTA\n5 - QUINTA\n6 - SEXTA\n7 - SABADO')

dias = str(input('Digite um numero correspondente a semana: '))

if dias == '1':
    print('Hoje é Domingo')

elif dias == '2':
    print('Hoje é Segunda')

elif dias == '3':
    print('Hoje é Terça')

elif dias == '4':
    print('Hoje é Quarta')

elif dias == '5':
    print('Hoje é Quinta')

elif dias == '6':
    print('Hoje é Sexta')

elif dias == '7':
    print('Hoje é Sabado')    

else: 
    quit('Dia da semana invalido')