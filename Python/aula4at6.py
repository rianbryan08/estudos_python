popu_a = 80000
popu_b = 200000
anos = 0

while popu_a <= popu_b:
    popu_a += popu_a * 0.03
    popu_b += popu_b * 0.015
    anos += 1

print(f'Serão necessarios {anos} anos para que população A passe ou se iguala população B')
    