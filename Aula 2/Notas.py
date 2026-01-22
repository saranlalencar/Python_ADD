nota_1 = float(input("Insira a nota:" ))
nota_2 = float(input("Insira a nota:" ))
nota_3 = float(input("Insira a nota:" ))

media = (nota_1 + nota_2 + nota_3) /3

print(f"A média é igual a: {media:.2f}")

if media >= 7:
    print(" Aprovado")
else:
    print("Reprovado")