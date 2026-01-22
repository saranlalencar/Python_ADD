# Crie um programa que pede a idade de 10 pessoas. 
# Armazene essas idades em uma lista e calcule a média de idade, a menor idade, a maior idade e quantas pessoas possuem idade maior ou igual a 30 anos.
# Crie uma lista antes das repetições
# Use o comando .append para adicionar elementos na lista

lista_idade = []
qtd_maior_que_30 = 0

for i in range (5):
    idades = int(input("Insira uma idade: "))
    lista_idade.append(idades)
    

media = sum(lista_idade) / len(lista_idade)
menor_idade = min(lista_idade)
maior_idade = max(lista_idade)

for idades in lista_idade:
    if idades >= 30:
        qtd_maior_que_30 += 1

print(f"{media},{menor_idade}, {maior_idade},{qtd_maior_que_30}")
