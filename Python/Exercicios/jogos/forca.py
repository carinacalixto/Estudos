def jogar():
    print('*****************')
    print('* Jogo da FORCA *')
    print('*****************')

    letras_escolhidas = []
    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    acertou = False
    enforcou = False
    repetida = False
    erros = 0

    while(not acertou and not enforcou): 
        print()
        print(letras_acertadas)
        chute = input('Escolha uma letra: ')
        if(chute not in letras_escolhidas):
            letras_escolhidas.append(chute)
            if(chute in palavra_secreta):
                posicao = 0
                for letra in palavra_secreta:
                    if (chute.lower() == letra.lower()):
                        letras_acertadas[posicao] = letra
                    posicao += 1
            else:
                erros += 1
                #     ___
                #    |   O
                #    |  /|\
                #    |  / \
                #   _|_
                print("ERROU!! \n")
                if(erros == 1):
                    print(" O")
                elif(erros == 2):
                    print(" O")
                    print(" |")
                elif(erros == 3):
                    print(" O")
                    print("/|")
                elif(erros == 4):
                    print(" O")
                    print("/|\\")
                elif(erros == 5):
                    print(" O")
                    print("/|\\")
                    print("/ ")
                elif(erros == 6):
                    print(" O")
                    print("/|\\")
                    print("/ \\")
        else:
            print("\nA letra {} já foi escolhida" .format(chute))
        acertou = "_" not in letras_acertadas
        enforcou = erros >= 6

    if (acertou):
        print("\nParabéns! Você VENCEU! \o/")
    elif(enforcou):
        print("\nVocê PERDEU! :(")

    print('\n****** FIM ******')