import os
import random

path = os.getcwd()+'\\Python\\Exercicios\\jogos\\forca\\palavras.txt'

# print(path)

# arquivo = open(path, 'w')

# arquivo.write('banana\n')
# arquivo.write('melancia\n')
# arquivo.write('morango\n')
# arquivo.write('manga\n')
# arquivo.write('uva\n')
# arquivo.write('pera\n')
# arquivo.write('abacaxi\n')
# arquivo.write('abacate\n')

# arquivo.close()

arquivo = open(path, 'r')

# arquivo.write('Não será possível escrever, pois foi aberto no modo "r"!!') #ERRO
# print('PRIMEIRA LEITURA')
# print(arquivo.read())

# print('SEGUNDA LEITURA')
# print(arquivo.read()) #Não consegue ler duas vezes, para tal, fechar e abrir o arquivo novamente

# print('TERCEIRA LEITURA')
# arquivo.close()
# arquivo = open(path, 'r')
# print(arquivo.read())

# print('**** LEITURA LINHA A LINHA ****')
# arquivo.close()
# arquivo = open(path, 'r')
# for linha in arquivo:
#       print(linha) #Acrescenta um \n após cada linha lida, logo como cada linha já possui um \n, ficam com 2x \n
# arquivo.close()

# print('**** LEITURA READLINE()  ****')
# arquivo.close()
# arquivo = open(path, 'r')
# linha = arquivo.readline()
# print(linha)

print('**** LEITURA ARQUIVO - Criação de lista de palavras ****')
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

print(palavras)

print(random.randrange(0,4))

arquivo.close()