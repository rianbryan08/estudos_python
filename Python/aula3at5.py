nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a primeira nota do aluno: '))

media = (nota1 + nota2) / 2

if media  == 10:
    print('Você foi aprovado com distinção, e sua nota foi de {}'.format(media))

elif media >= 7:
    print('Você foi aprovado, e sua nota foi de {}'.format(media))

else:
    quit('Você foi reprovado, e sua nota foi de {}'.format(media)) 