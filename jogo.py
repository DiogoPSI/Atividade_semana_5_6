import escolher_palavra


def jogo():
    dif = input("Escolha a dificuldade: \n1 - Fácil 2 - Normal 3 - Dificil\n")

    tentativas_restantes = 6
    palavra = escolher_palavra.defenir_palavra(dif)
    if isinstance(palavra, int):
        print("Opção invalida")
        exit()
    tentativa = "*" * len(palavra)
    acertou = None

    while tentativa != palavra and tentativas_restantes != 0:
        print(desenhar_enforcado(6-tentativas_restantes))
        print("Palavra: " + tentativa)
        print("Tentativas restantes: " + str(tentativas_restantes))
        letra = input("Introduza uma letra: ")
        for i in range(len(palavra)):
            if letra == palavra[i]:
                tentativa = tentativa[:i] + letra + tentativa[i + 1:]
                acertou = True
        if acertou:
            print(letra + " pertence a palavra!")
            acertou = False
        else:
            tentativas_restantes -= 1
            print(letra + " não pertence a palavra")

    if palavra == tentativa:
        print(desenhar_enforcado(6 - tentativas_restantes))
        print("Palavra: " + palavra)
        print("Venceu!")
    else:
        print(desenhar_enforcado(6))
        print("Perdeu!")
        print("Palavra: " + palavra)
    jogar_novamente()


def jogar_novamente():
    op = input("Jogar Novamente? 1 - Sim 2 - Não\n")
    if op == "1":
        jogo()
    elif op == "2":
        print("Até à proxima!")
        exit()
    else:
        print("Opção Invalida")
        jogar_novamente()


def desenhar_enforcado(pos):
    enforcado = [
        """
               --------
               |      |
               |      
               |    
               |      
               |     
               -""",
        """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -""",
        """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -""",
        """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -""",
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -""",
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -""",
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -"""
    ]
    return enforcado[pos]


jogo()
