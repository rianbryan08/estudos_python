peso = float(input("Digite o peso do peixe que você pescou: "))

if (peso > 50):
    print("Seu peixe passou o peso estabelecido pelo regulamento, você terá que pagar a multa de R$4.00 por quilo excedente")
    calc_peixe = peso - 50
    multa = calc_peixe * 4     
    print(f"O calculo de excesso do peixe foi de: {calc_peixe:.2f}")
    print(f"O valor da multa ficou em: {multa:.2f} ") 
else: 
    quit("O seu peixe está com o peso estabelecido pelo regulamento, você não precisara pagar a multa")
                