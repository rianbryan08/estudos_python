num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % 2 == 0:
    num1 += 1

while num1 <= num2:
    print(num1, end = ' ')
    num1 += 2
