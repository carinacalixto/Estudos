numero_secreto = 42

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

for rodada in range(0,tentativas):

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