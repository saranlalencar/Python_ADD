# 1. (BÁSICO) Crie um programa que pede o nome de 5 frutas e ao final imprime uma lista numerada com o nome das frutas. Exemplo:

# 1. Fruta 1
# 2. Fruta 2
# 3. Fruta 3
# 4. Fruta 4
# 5. Fruta 5

# 1. (AVANÇADO) Continue o programa anterior e agora ao lado do nome de cada fruta acrescente o texto "é saudável!"
lista_frutas = []

for i in range(3):
    frutas = input("Insira o nome da fruta: ")
    lista_frutas.append(frutas)

contador = 0
for fruta in lista_frutas:
    print(f"{contador+1}, {frutas}")
    contador += 1









