s = 0
for i in range(1, 7):
    n = int(input('Digite o {} valor: '.format(i)))
    if n % 2 == 0:
        s += n
print('A soma foi = {}'.format(s))