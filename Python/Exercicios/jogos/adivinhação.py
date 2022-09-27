import random

def jogar():
	numero_secreto = random.randint(0, 1001)
	total_pontos = 1000

	dificuldade = int(input("Digite o número da dificuldade: \n1) Fácil\n2) Médio\n3) Difícil\n\n"))

	facil = dificuldade == 1
	medio = dificuldade == 2
	dificil = dificuldade == 3

	if facil:
		tentativas = 20
	elif medio:
		tentativas = 10
	elif dificil:
		tentativas = 5
	else:
		exit()

	for rodada in range(0,tentativas):

		print("***********************")
		print("* Jogo da Adivinhação *")
		print("***********************")
		print("Tentativa {} de {}...\nVocê possui {} pontos" .format(rodada+1,tentativas,total_pontos))
		chute = int(input("Digite o seu número: "))

		acertou = chute == numero_secreto
		maior = chute > numero_secreto

		if acertou:
			print("Você ACERTOU!!!")
			break
		elif maior:
			total_pontos = total_pontos - abs(chute - numero_secreto)
			print("Você errou! :( \nO seu chute foi MAIOR que o número secreto.")
			
		else:
			total_pontos = total_pontos - abs(chute - numero_secreto)
			print("Você errou! :( \nO seu chute foi menor que o número secreto.")
			
	print("FIM\n\nVocê finalizou com {} pontos" .format(total_pontos))