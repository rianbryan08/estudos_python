print('\tDigite o numero que deseja saber a tabuada\n')

n = int(input('Digite um valor: '))
for i in range(1, 11):
    print(f'{n} X {i} = {n*i}')