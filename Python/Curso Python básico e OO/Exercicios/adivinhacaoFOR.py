numero_secreto = 42
tentativas = 3

for rodada in range(0,3):

	print("***********************")
	print("* Jogo da Adivinhação *")
	print("***********************")
	print("Tentativa {} de {}..." .format(rodada+1,tentativas))
	chute = int(input("Digite o seu número: "))

	acertou = chute == numero_secreto
	maior = chute > numero_secreto

	if acertou:
		print("Você ACERTOU!!!")
		break
	elif maior:
		print("Você errou! :( \nO seu chute foi MAIOR que o número secreto.")
	else:
		print("Você errou! :( \nO seu chute foi menor que o número secreto.")