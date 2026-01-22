# Crie um programa que recebe a quantidade de candidatos que prestaram uma prova de concurso. 
# Depois disso, para cada candidato, peça o nome e a nota (0 a 100) obtida no concurso
# se o candidato tiver obtido nota maior ou igual a 80, imprima na tela "{nome} - Aprovado". 
# Ao final exiba um resumo contendo Total de Aprovados, Total de Reprovados e Média Geral. 
# Bônus: Antes do resumo exiba a lista candidatos com Nome - Nota - Situação.
candidatos = []
soma_notas = 0
aprovados = 0
reprovados = 0
quant_candidatos = int(input("Insira a quantidade de candidatos: "))

for i in range(quant_candidatos):
    nome = str(input("Insira o seu nome: "))
    nota = int(input("Insira a nota (0-100): "))
    soma_notas += nota
    if nota >= 80:
        situacao = "aprovado"
        print(f"Candiato: {nome} aprovado!")
        aprovados += 1
    else:
        situacao = "reprovado"
        print(f"Candidato: {nome} reprovado!")
        reprovados += 1
    candidatos.append((nome, nota, situacao))

media = soma_notas / quant_candidatos
    

print("\n----- LISTA DE CANDIDATOS -----")
for nome, nota, situacao in candidatos:
    print(f"{nome} - {nota} - {situacao}")

print("\n----- RESUMO -----")
print(f"Total de Aprovados: {aprovados}")
print(f"Total de Reprovados: {reprovados}")
print(f"Média Geral: {media:.2f}")