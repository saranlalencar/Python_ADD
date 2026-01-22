# Crie um programa que pede o preço de 5 produtos válidos e exibe o total. 
# Aceite apenas produtos em que o preço informado está entre 10 reais e 100 reais.

qtd_produtos = 0
soma = 0

while qtd_produtos < 5:
    preco = int(input(f"Informe o preço do produto: "))
    soma += preco
    if (preco > 10 and preco < 100):
        soma += preco
        qtd_produtos += 1
        
    else:
        print("Insira um valor entre 10 e 100!")

print(f"A soma é: {soma}")
       