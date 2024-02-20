print("\tFolha de Pagamento\n")

salario_hora = float(input("Salário/hora: R$ "))
horas_mes = int(input("Horas Trabalhadas no Mês: "))

salario_bruto = salario_hora * horas_mes
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (IR + INSS + sindicato)

print(" ")
print(f"Salário Bruto: R${salario_bruto:.2f}")
print("")
print("\tDescontos\n")
print(f"IR: R${IR:.2f}")
print(f"INSS: R${INSS:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(" ")
print(f"Salário Líquido: R${salario_liquido:.2f}")