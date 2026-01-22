# Crie um programa de cálculo de total de venda. Peça o valor de 5 produtos diferentes (somente o preço) e a quantidade comprada. 
# Ao final exiba o valor total da compra.
# Bônus: Peça o nome dos produtos e ao final exiba a nota fiscal da compra contendo Produto - Preço - Quantidade - Total

total = 0
precos = []
produtos = []
quantidade = []
for i in range (2):
     produto = str(input("Insira o nome do produto: "))
     produtos.append(produto)
     preco = float(input("Insira o valor do produto: R$ "))
     quant = int(input("Insira a quantidade comprada: "))
     quantidade.append(quant)
     precos.append(preco * quant)
     

total = sum(precos)
print("\n----- NOTA FISCAL -----")
for i in range(len(produtos)):
    print(f"{produtos[i]} - R$ {precos[i]:.2f} - {quantidade[i]} un")
print(f"Total: R$ {total:.2f}")
           


