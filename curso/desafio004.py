algo = (input('Digite algo: '))

print(type(algo))
print('É alfabético?', algo.isalpha())
print('É Numérico?', algo.isnumeric())
print('É alfanumérico?', algo.isalnum())
print('Está tudo escrito em mainúsculo?', algo.isupper())
print('Está tudo escrito em minúsculo?', algo.islower())
print('É um número decimal?', algo.isdecimal())
print('É um identificador?', algo.isidentifier())
print('Pode ser impresso?', algo.isprintable())
print('Começa com letras maiúsculas e termina com minúsculas?', algo.istitle())
print('É um dígito?', algo.isdigit())
print('Contém apenas espaços?', algo.isspace())