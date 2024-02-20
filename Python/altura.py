print("Você é homem ou mulher?")
genero = str(input("Qual o seu sexo?: "))

if (genero == "homem"):
    altura = float(input("Dgitei sua altura: "))
    result = (72.7*altura) - 58
    print(f"O seu peso ideal é de: {result}")

elif (genero == "mulher"):
    altura = float(input("Dgitei sua altura: "))
    result = (62.1*altura) - 44.7
    print(f"O seu peso ideal é de: {result}")    

else:
    quit("Não foi informado qual o seu sexo")