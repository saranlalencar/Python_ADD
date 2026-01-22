# Crie um programa que recebe números inteiros, até que a soma desses números seja maior ou igual 100. 
# Fraseamento alternativo: Enquanto a soma dos números for menor que 100, receba novos números inteiros.
soma = 0
while soma < 100:
    num = int(input("Insira um número: "))
    soma += num
print(f"A soma dos números é: {soma}")

