print('\tEscolha uma das opções\n')
print('1 - Verificar se o número é par ou impar\n'
      '2 - Identificar o maior número dentro 5 numeros\n'
      '3 - Criar uma tabuada com o número digitado\n'
      '4 - Sair do programa')

escolha = 0

while escolha != 4:
    escolha = int(input('Digite a sua escolha: \n'))

    if escolha == 1:
        n1 = int(input('Digite um numero: '))
        if n1 % 2 == 0:
            print('Esse numero é par')
        else:
            print('Esse numero é impar')

    i = 0
    maior = 0
    if escolha == 2:
        for i in range(1, 6):
            n2 = int(input('Digite o '+str(i)+'° número: '))
            if n2 > maior:
                maior = n2
        print('O maior número digitado é {}'.format(maior))

    j = 0
    if escolha == 3:
        n3 = int(input('Digite o número para a tabuada: '))
        for j in range(1, 11):
            print('{} x {} = {}'.format(n3, j, (n3 * j)))

    if escolha == 4:
        print('Adeus')

    if escolha > 4 or escolha <= 0:
        print('Escolha invalida')
