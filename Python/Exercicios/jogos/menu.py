import forca
import adivinhação

# print(type(forca)) # Tipo módulo

print('***************************************')
print('************ MENU DE JOGOS ************')
print('***************************************')
print('1) Adivinhação')
print('2) Forca')

escolha = int(input('Digite o número do jogo que deseja jogar (1 ou 2): '))

if escolha == 1:
    adivinhação.jogar()
elif escolha == 2:
    forca.jogar()
else:
    print('Escolha inválida!')