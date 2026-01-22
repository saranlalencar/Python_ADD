# Criar um programa de cálculo de desconto. O programa deverá receber o valor da compra, a idade do cliente e a cidade do cliente.
# Ao final o programa deverá exibir o valor do desconto aplicado na compra e o novo valor atualizado. 
# Os critérios de desconto são:

#1: Se o cliente tiver mais que 30 anos de idade - Aplicar 5% de desconto

#2: Se o cliente for da cidade Fortaleza - Aplicar 5% de desconto
#   Se o cliente for da cidade Maranguape - Aplicar 10% de desconto
#   Se o cliente for da cidade Morada Nova - Aplicar 20% de desconto


desconto = 0

print("Forneça as informações abaixo para calcular o desconto da venda!")
valor_compra = float(input("Insira o valor da compra: "))
idade = int(input("Insira a sua idade:"))
cidade = str(input("Insira a sua cidade: ")).upper

if idade >= 30:
    print("Desconto de idade concedido! ✔️")
    desconto += 0.05
else:
    print("Desconto de idade não foi concedido! ❌")

if cidade == "FORTALEZA":
    desconto += 0.05
elif cidade == "MARANGUAPE":
    desconto += 0.10
elif cidade == "MORADA NOVA":
    desconto += 0.20
#3: Se o valor total da compra superar 1000 - Aplicar 10% de desconto
#   Se o valor total da compra superar 2000 - Aplicar 15% de desconto

# Os descontos devem ser acumulativos e será a soma dos descontos aplicados.

if valor_compra >= 1000 and valor_compra < 2000:
    desconto = 0.10
elif valor_compra >= 2000:
    desconto = 0.15

valor_desconto = valor_compra * desconto
total = valor_compra - valor_desconto

print(f'''
Informações da Venda:
      
      Valor Original: R$ {valor_compra:.2f}
      Desconto Aplicado: {desconto*100}%
      Valor Descontado: R$ {valor_desconto:.2f}
      Valor Líquido: R$ {total:.2f}
''')



