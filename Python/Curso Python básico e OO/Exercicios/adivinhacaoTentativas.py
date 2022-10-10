numero_secreto = 42
tentativas = 3
rodada = 1
chance = rodada <= tentativas

while (chance):

	print("***********************")
	print("* Jogo da Adivinhação *")
	print("***********************")
	print("Tentativa {} de 3..." .format(rodada))
	chute = int(input("Digite o seu número: "))
	
	rodada+=1

	acertou = chute == numero_secreto
	maior = chute > numero_secreto
	#menor = chute < numero_secreto
	chance = rodada <= tentativas

	if acertou:
		print("Você ACERTOU!!!")
		break
	elif maior:
		print("Você errou! :( \nO seu chute foi MAIOR que o número secreto.")
	else:
		print("Você errou! :( \nO seu chute foi menor que o número secreto.")