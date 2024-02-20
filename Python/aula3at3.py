sexo = str(input('Digite qual o seu sexo F para Feminino ou M para masculino: '))

if sexo == 'M':
    print('{} sexo Masculino'.format(sexo))

elif sexo == 'F':
    print('{} sexo Feminino'.format(sexo))

else:
    quit('Sexo invalido')