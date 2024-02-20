num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
total = 0

while num1 <= num2:
    total += num1
    num1 += 1

print("Resultado = ", total)
