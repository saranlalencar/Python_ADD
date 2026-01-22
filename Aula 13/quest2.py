# 2. (BÁSICO) Crie um programa que pede o nome de um aluno, seu cpf e idade além de 4 notas VÁLIDAS (0 a 10) desse aluno.
#  Ao final imprima uma ficha com as informações pessoais desse aluno, sua média, situação(aprovado, recuperação ou reprovado)
#  e um boletim com as notas inseridas em sequência. Exemplo:

nome = input("Insira o nome do aluno: ")
cpf = int(input("Insira o CPF do Aluno: "))
cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
idade = int(input("Insira a idade: "))

lista_notas = []

for i in range(4):
    notas = float(input("Insira as notas do aluno: "))
    lista_notas.append(notas)
    
media = sum(lista_notas) / len(lista_notas)

if media >= 7:
    situacao = "Aprovado"
elif media <= 4:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"""
==================================================
FICHA DO ALUNO
==================================================
Nome: {nome}
CPF: {cpf_formatado}
Idade: {idade}
--------------------------------------------------
BOLETIM ESCOLAR
Nota 1: {lista_notas[0]}
Nota 2: {lista_notas[1]}
Nota 3: {lista_notas[2]}
Nota 4: {lista_notas[3]}
--------------------------------------------------
Média: {media}
Situação: {situacao}
==================================================
"""
)