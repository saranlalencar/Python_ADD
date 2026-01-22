# Crie um programa que pede um palpite (0 a 100) para um jogador e repete caso o jogador erre o número secreto. 
# Se o jogador acertar, o programa é encerrado e é exibido na tela quantos palpites foram necessários para acertar.

# Missão 1: Ao errar, dê uma dica para o jogador. Informe se o número secreto é maior ou menor que o palpite.

# Missão 2: Encerre o jogo após 3 tentativas. Caso o jogador não acerte, exiba uma mensagem de Derrota.

#Missão 3: Faça com que o número secreto seja aleatório e o número mude sempre que for iniciado um novo jogo

#Missão 4: Ao final do jogo, pergunte se o jogador deseja jogar novamente e reinicie o jogo
import random

while True:
    numero_secreto = random.randint(0,100)
    tentativas = 0

    while True:
     palpite = int(input("Insira o seu palpite de 1 a 100: "))
     
    if palpite == num_sec:
       print("Você acertou!")
       break
    else:
       print("Você errou!")

       if palpite < numero_secreto:
                print("O número secreto é maior!")
            else:
                print("O número secreto é menor!")

            if tentativas >= 3:
                print("Você chegou ao fim de suas tentativas!")
                break
        

    print("Fim de Jogo!")
    print(f"O número era: {numero_secreto}")

    continuar = input("Deseja continuar? (s/n)")

    if continuar != "s":
        break