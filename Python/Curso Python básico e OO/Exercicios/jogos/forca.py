import random
import os

def imprime_mensagem_abertura():
    print('*****************')
    print('* Jogo da FORCA *')
    print('*****************')

def carrega_palavra_secreta():
    path = os.getcwd()+'\\Python\\Exercicios\\jogos\\forca\\palavras.txt'

    arquivo = open(path, 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    num_palavra = random.randrange(0,len(palavras))

    palavra_secreta = palavras[num_palavra].upper()
    return palavra_secreta

def inicia_letras_acertadas(psw):
    return ['_' for letra in psw]

def pede_chute():
    chute = input('Escolha uma letra: ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_erro(err):
    err += 1
    print("ERROU!! \n")
    if(err == 1):
        print('  ___')
        print(" |   O")
        print(" | ")
        print(" | ")
        print('_|_')
    elif(err == 2):
        print('  ___')
        print(" |   O")
        print(" |   |")
        print(" | ")
        print('_|_')
    elif(err == 3):
        print('  ___')
        print(" |   O")
        print(" |  /|")
        print(" | ")
        print('_|_')
    elif(err == 4):
        print('  ___')
        print(" |   O")
        print(" |  /|\\")
        print(" | ")
        print('_|_')
    elif(err == 5):
        print('  ___')
        print(" |   O")
        print(" |  /|\\")
        print(" |  / ")
        print('_|_')
    elif(err == 6):
        print('  ___')
        print(" |   O")
        print(" |  /|\\")
        print(" |  / \\")
        print('_|_')
    return err

def finaliza_jogo(ganhou, perdeu, psw):
    if (ganhou):
        print()
        print('A palavra secreta era: ', psw)
        print("\nParabéns! Você VENCEU! \o/")
    elif(perdeu):
        print()
        print('A palavra secreta era: ', psw)
        print("\nVocê PERDEU! :(")
    print('\n****** FIM ******')

def jogar():

    imprime_mensagem_abertura()

    letras_escolhidas = []
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    acertou = False
    enforcou = False
    palavra_nova = True
    
    erros = 0

    while(not acertou and not enforcou): 
        print()
        print(letras_acertadas)
        chute = pede_chute()
        palavra_nova = chute not in letras_escolhidas
        if(palavra_nova):
            letras_escolhidas.append(chute)
            if(chute in palavra_secreta):
                marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            else:
                erros = imprime_erro(erros)
        else:
            print("\nA letra {} já foi escolhida" .format(chute))
        acertou = "_" not in letras_acertadas
        enforcou = erros >= 6

    finaliza_jogo(acertou, enforcou, palavra_secreta)