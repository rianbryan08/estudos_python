nota = -1

print ('\tDigite um valor entre 0 e 10\n')
while nota < 0 or nota > 10:
    nota = float(input("Digite um numero: "))
    
    if nota < 0 or nota > 10:
        print("Valor inválido! Tente novamente.")
  