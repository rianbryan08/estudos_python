num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

total = 0
for i in range(num1, num2+1):
    total += i

print("Resultado =", total)