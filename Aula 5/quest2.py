# Crie um programa que pede um nome de usuário e uma senha. 
# Se o nome de usuário for "admin" e a senha for "password", exiba na tela "Acesso Concedido", se não exiba "Acesso Negado"

usuario = input("Insira o login: ").upper()
senha = input("Insira a senha:").upper()

if usuario == "ADMIN" and senha == "PASSWORD":
    print("Acesso concedido")
else:
    ("Acesso negado!")
    
