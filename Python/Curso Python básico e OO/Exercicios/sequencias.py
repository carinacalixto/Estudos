import os
clear = lambda: os.system('cls')
clear()

# Dada a lista abaixo:
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print(lista)

# Imprima o maior elemento
print("O maior elemento: ",max(lista))
# ou
maior = lista[0]
for i in range(0,len(lista)):
    if(lista[i] > maior):
        maior = lista[i]
print("Outra forma de encontrar o maior elemento: ", maior)

# Imprima o menor elemento
print("O menor elemento: ", min(lista))
# ou
menor = lista[0]
for i in range(0,len(lista)):
    if(lista[i] < menor):
        menor = lista[i]
print("Outra forma de encontrar o menor elemento: ", menor)

# Imprima os números pares
pares = []
for i in lista:
    if (i%2==0):
        pares.append(i)
print("Os pares: ", pares)
        
# Imprima o número de ocorrências do 1 elemento da lista
primeiro = lista[0]
ocorrencias = 0
for a in lista:
    if (a == primeiro):
        ocorrencias += 1
print("Ocorrencias do 1 elemento na lista: ", ocorrencias)

# Imprima a média dos elementos
soma = 0
for n in lista:
    soma += n
media = soma/len(lista)
print("A média dos elementos: ",media)

# Imprima a soma dos elementos de valor negativo
somaneg = 0
for x in lista:
    if (x<0):
        somaneg += x
print("A soma dos elementos negativos: ", somaneg)