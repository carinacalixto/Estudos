print("***********************")
print("* Jogo da Adivinhação *")
print("***********************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))
print("Você digitou: {}" .format(chute))

acertou = chute == numero_secreto
maior = chute > numero_secreto
#menor = chute < numero_secreto

if acertou:
	print("Você ACERTOU!!!")
elif maior:
	print("Você errou! :( \nO seu chute foi MAIOR que o número secreto.")
else:
	print("Você errou! :( \nO seu chute foi menor que o número secreto.")