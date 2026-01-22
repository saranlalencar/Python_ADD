# Crie um programa que exibe os 10 primeiros números divisíveis por 6.

num = 1
qtd_divisiveis = 0

while qtd_divisiveis < 10:
    if num % 6 == 0:
        print(num)
        qtd_divisiveis += 1
    num += 1