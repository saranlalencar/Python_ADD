# Crie um programa que recebe a idade de um usuário. Categorize se a pessoa é jovem ou adulto seguindo o critério abaixo:
# Menor que 18 anos, Jovem
# 18 anos ou mais, Adulto

idade = int(input("Digite sua idade: "))

if idade <= 18 and idade >= 0:
    print("Você é jovem")
elif idade >= 18 and idade < 65:
    print("Você é adulto")
elif idade >= 65:
    print("Você é idoso")