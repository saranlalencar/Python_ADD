# Crie um programa que pede 5 números ao usuário. Ao final determine e imprima o maior número digitado.
# Bônus: Ao final exiba na tela todos os números que foram digitados

num = 0
numeros = []
maior_num = 0
for i in range(3):
    num = int(input("Insira um número: "))
    numeros.append(num)
    if num > maior_num:
        maior_num = num
    
 
print(f"O maior número é: {maior_num}")
print(f"Números inseridos: {numeros}")


    