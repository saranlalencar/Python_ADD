# Crie um programa que exibe um menu com 3 charadas e uma opção de sair. 
# Ao escolher uma das opções do menu, exibe a charada escolhida e pede uma resposta ao jogador. 
# Se o jogador acertar é exibida uma mensagem de vitória, se o jogador errar é exibida uma mensagem de derrota. 
# Independente do resultado, volta ao menu depois do palpite.
while True:
    print('''
      Escolha uma opção:
      1. charada 
      2. charada 
      3. charada 
      0. Sair ''')
    op = int(input("Insira a opção desejada: "))
    
    if op == 1:
        print("----- CHARADA 1 -----")
        print("O que é o que é surdo e mudo e conta tudo?")
        palpite = input("Digite seu palpite: ").lower()

        if palpite == "livro":
            print("A resposta está correta!")
        else: 
            print("Você errou!")
    elif op == 2:
         print("----- CHARADA 2 -----")
         print("Quanto mais você tira, maior ele fica?")
         palpite = input("Digite seu palpite").lower()
         if palpite == "buraco":
             print("Você acertou!")
         
         else: 
             print("Você errou!")
    elif op == 3:
        print("----- CHARADA 3 -----")
        print("Anda sem pés, fala sem boca e nunca se cansa?")
        palpite = input("Insira seu palpite: ").lower()
        if palpite == "eco":
            print("Você acertou!")
        else:
            print("Você errou!")

    


    


