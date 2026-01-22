# Crie um programa que recebe um número e depois exibe a tabuada desse número.
i = 1
num = int(input("Insira um número inteiro"))

while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i += 1
