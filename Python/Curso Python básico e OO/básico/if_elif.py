num = 42
chute = int(input('Digite um número: '))

acertou = chute == num
maior = chute > num
menor = chute < num

##if chute == num:
if acertou:
	print("Você acertou!")
	print("PABABÉNS! \\o/")
#else:
	#if chute > num:
##elif chute > num:
elif maior:
	print("O seu chute foi MAIOR que o número secreto >>>>>")
	#else:
##elif chute < num:
###elif menor:
else:
	print("O seu chute foi menor que o número secreto <<<<<")