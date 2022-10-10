numero_secreto = 42
tentativas = 3
rodada = 1
chance = rodada <= tentativas
errar = True

while (errar):

	print("***********************")
	print("* Jogo da Adivinhação *")
	print("***********************")
	print("Tentativa #{}..." .format(rodada))
	chute = int(input("Digite o seu número: "))
	
	acertou = chute == numero_secreto
	maior = chute > numero_secreto
	#menor = chute < numero_secreto
	chance = rodada <= tentativas
	errar = chute != numero_secreto

	if acertou:
		print("Você ACERTOU!!!")
		break
	elif maior:
		print("Você errou! :( \nO seu chute foi MAIOR que o número secreto.")
	else:
		print("Você errou! :( \nO seu chute foi menor que o número secreto.")
		
	rodada+=1

print("Você acertou em {} tentativas" .format(rodada))