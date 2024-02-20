popu_a = int(input("Informe a população do pais A: "))
popu_b = int(input("Informe a população do pais B: "))
taxa_a = float(input("Informe a taxa de crescimento da população A (em %): "))
taxa_b = float(input("Informe a taxa de crescimento da população B (em %): "))

anos = 0
while   popu_a <= popu_b:
    popu_a +=  popu_a * (taxa_a / 100)
    popu_b += popu_b * (taxa_b / 100)
    anos += 1

print(f"São necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")