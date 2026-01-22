# Criar um programa de adivinhar o número. O programa deve conter um número secreto e deverá pedir ao usuário um palpite (0 a 10), se o usuário acertar o palpite imprimir na tela vitória, se não imprimir na tela derrota.
# - Melhore o programa para exibir na tela, quando o usuário errar, se o palpite era maior ou menor que o número secreto
# - Permita que o jogador tente 3 vezes (sem usar repetições)

import random
numeroSecreto = random.randint(0,10)

palpite = int(input(" Você possui 3 chances! Digite o seu palpite: "))

if palpite == numeroSecreto:
    print(f"Você venceu de primeira! Você chutou {palpite} e o número secreto era {numeroSecreto}!")
else:
    print(f"Você perdeu! Você chutou {palpite}. Tente novamente!")
if numeroSecreto < palpite:
    print("Seu palpite foi mais alto que o número secreto!")
else:
    print("Seu palpite foi mais baixo que o número secreto!")

palpite = int(input("Digite seu novo palpite de 0 a 10:"))

if numeroSecreto == palpite:
    print("Parabéns! Você acertou")
if numeroSecreto < palpite:
    print("Seu palpite foi mais alto que o número secreto!")
else:
    print("Seu palpite foi mais baixo que o número secreto!")

palpite = int(input("Digite o seu palpite: "))

if numeroSecreto == palpite:
    print("Parabéns! Você acertou")
if numeroSecreto < palpite:
    print("Seu palpite foi mais alto que o número secreto!")
else:
    print("Seu palpite foi mais baixo que o número secreto!")

print("Fim de Jogo!")

print(f"O número secreto era {numeroSecreto}")