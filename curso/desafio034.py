sexo = str(input('Qual o seu sexo?\nM - Masculinos\nF- Feminino\n')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('dados invalidos informe o sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
