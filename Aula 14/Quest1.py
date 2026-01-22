# 3. Crie um programa que recebe uma lista de valores de temperatura. 
# O usuário deverá escrever cada temperatura até que escreva "SAIR" no campo de cadastro.
#  Ao finalizar exibir a lista de temperaturas, a maior temperatura, a menor temperatura e a média de temperatura.
temp_lista = []
maior = None
menor = None

while True: 
    op = input(''' Digite "1" para inserir a temperatura: 
           Digite "2" para sair: ''')
    if op == "1":
        temp = float(input("Insira a temperatura em °C: "))
        temp_lista.append(temp)
        if maior is None and menor is None:
            maior = temp
            menor = temp
        else:
            if temp > maior:
                maior = temp
            elif temp < menor:
                menor = temp
    elif op == "2":
        print("Encerrando...")
        break
    else:
        print("Insira uma opção válida!")

media = sum(temp_lista) / len(temp_lista)
print(f"{temp_lista}, media: {media}.maior: {maior}, menor: {menor}")

    

    

    








# 3. (AVANÇADO) Ao exibir as temperaturas ordene-as de forma decrescente (maior para menor). 
# Além disso modifique o programa para pedir 12 temperaturas, cada uma referente a um mês de 2025, 
# ao final inclua nas informações de Maior Temperatura e Menor Temperatura o nome do mês correspondente.