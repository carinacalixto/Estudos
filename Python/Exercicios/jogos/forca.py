print('*****************')
print('* Jogo da FORCA *')
print('*****************')

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
acertou = False
enforcou = False

while(not acertou and not enforcou):
    print(letras_acertadas)
    chute = input('Escolha uma letra: ')
    posicao = 0
    for letra in palavra_secreta:
        if (chute.lower() == letra.lower()):
            letras_acertadas[posicao] = letra
        posicao = posicao + 1

print('****** FIM *******')