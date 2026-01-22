# Crie um programa que pede um palpite (0 a 100) para um jogador e repete caso o jogador erre o número secreto.
#  Se o jogador acertar, o programa é encerrado e é exibido na tela quantos palpites foram necessários para acertar.

num_sec = 57

palpite = int(input("Insira o seu palpite: "))
tentativas = 1

while palpite != num_sec:
    print("Você errou!")
    palpite = int(input("Digite um número de 0 a 100:"))
    tentativas += 1

print(f"Você acertou! Tentativas {tentativas}")
