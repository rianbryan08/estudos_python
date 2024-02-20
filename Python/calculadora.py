print("Digite o numero 1 para somar: ")
print("Digite o numero 2 para subtração")
print("Digite o numero 3 para divisão")
print("Digite o numero 4 para multiplicação")

resposta_user = input("qual opção você vai querer fazer?: ")

if (resposta_user == "1"):
    print("Você selecionou a opção para somar")
    num1 = float(input("Informe o primeiro numero: "))
    num2 = float(input("Informe o segundo numero: "))
    result= num1+num2
    print(f"O resultado é: {result}")

elif (resposta_user == "2"):
    print("Você selecionou a opção para subtração")
    num1 = float(input("Informe o primeiro numero: "))
    num2 = float(input("Informe o segundo numero: "))
    result= num1-num2
    print(f"O resultado é: {result}")

elif (resposta_user == "3"):
    ("Você selecionou a opção para divisão")
    num1 = float(input("Informe o primeiro numero: "))
    num2 = float(input("Informe o segundo numero: "))
    result= num1/num2
    print(f"O resultado é: {result}")

elif (resposta_user == "4"):
    print("Você selecionou a opção para multiplicação")
    num1 = float(input("Informe o primeiro numero: "))
    num2 = float(input("Informe o segundo numero: "))
    result= num1*num2
    print(f"o resultado é: {result}")

else:
    quit("Nenhuma opção valida foi selecionada") 