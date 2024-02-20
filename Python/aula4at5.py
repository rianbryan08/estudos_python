user = str(input('Digite seu usuário: '))
senha = str(input('Digite sua senha: '))

while user == senha:
    print('ERRO! Usuario não pode ser igual a senha!')
    senha = input('Digite novamente sua senha: ')
    print('senha válida')