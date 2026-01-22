# Crie um programa de cálculo de notas. O programa deverá pedir ao usuário as 4 notas de um aluno (usar for)
#  e ao final deverá exibir média e situação do aluno.
# >= 7 - Aprovado
# >= 4 and < 7 - Recuperação
# < 4 - Reprovado
# Bônus: Peça ao usuário quantas notas ele deseja digitar. Utilize no cálculo de média somente notas válidas (0 a 10)

notas = []
for i in range(4):
    nota = float(input("Insira a nota: "))
    notas.append(nota)
    
media = sum(notas) / len(notas)
print(f'''
      Notas: {notas}
      A media é: {media}''')

if media >= 7:
    print("Aprovado!")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado!")
