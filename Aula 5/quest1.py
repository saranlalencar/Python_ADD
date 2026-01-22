# Crie um programa que pede dois números (float) ao usuário, além disso pede também uma operação (+, -, *, /).
#  Imprima na tela a operação e o resultado da operação matemática escolhida.
num1 = float(input("Insira o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Insira o segundo número: "))

if operacao == "+":
    resultado = num1 + num2 
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
else:
     print("Escolha uma operação válida!")
