# Crie um programa para realização de cadastro de funcionários. O programa deverá pedir o nome de um funcionário até que seja escrito a palavra "SAIR".
#  Ao final esse programa deve informar quantos funcionários foram cadastrados, além disso deve exibir uma lista de funcionários.
cadastro_funcionarios = []
qtd_funcionarios = 0 
print('''
      Escolha uma opção:
      1. Cadastrar funcionário 
      2. Visualizar lista de funcionário 
      3. Visualizar quantidade de funcionários
      4. Voltar ao menu
      0. Sair ''')
op = str(input("Insira a opção desejada: ")).lower()

while True:
   
    if op == "1":
        novo_funcionario = input("Insira o nome do funcionário: ")
        cadastro_funcionarios.append(novo_funcionario)
        qtd_funcionarios += 1
    elif op == "4":
            print('''
      Escolha uma opção:
      1. Cadastrar funcionário 
      2. Visualizar lista de funcionário 
      3. Visualizar quantidade de funcionários 
      0. Sair ''')
    op = str(input("Insira a opção desejada: ")).lower()
    if op == 2:
        print(f"Lista de funcionários: ")
    elif op == 3:
        print ("Lista quantidade de funcionários: ")
    elif op == 0:
        print("Saindo do programa...")
    else: 
        print("Escolha uma opção válida!")
