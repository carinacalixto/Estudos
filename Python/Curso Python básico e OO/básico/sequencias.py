import os
clear = lambda: os.system('cls')

#"""
# Lista e operações com lista: 

lista = ['c', 'a', 'r', 'i', 'n', 'a']
#lista = list('carina')
print(lista)
print(sorted(lista))
print(type(lista))
print( 'f' not in lista) #True
print( 'c' in lista) #True
print( lista * 3 )
print( lista [:4])
print( lista [:-4])
print(lista[5]) #a
print(lista[-1]) #a
print(len(lista))
print(lista[-len(lista)]) #c
print(lista.count('c'))

lista1 = [1, 2, 3, 4]
print(lista1)
lista2 = ['Pyhton', 'C', 'Java', 'C#', 'C++', 'Ruby']
print(lista2)
lista_hetereogenica = ['Python', 1, 2.2, 'Java', 3, 'Ruby', 4.4, 5]
print(lista_hetereogenica)

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes = int(input('\nEscolha um mês (1-12): '))
print('O mes escolhido é {}\n'.format(meses[mes-1]))

#"""


#"""

# Tuplas e operações com tuplas:
#dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
dias = 'domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'
print(type(dias))
print(sorted(dias))
p = tuple('Python')
print(p)
#t1 = tuple(lista1)
#print(t1)
#dias.append('sexta-feira') # ERRO!!
#dias[5] = 'sexta-feira' # ERRO!!
# Não se pode modificar uma TUPLA, porém pode-se modificar uma LISTA dentro de uma TUPLA
idades = [36,37,3]
tupla = ('Carina', 'Victor', 'Caipirinha', idades)
print(tupla)
idades[2] = 2
print(tupla)

#"""


#"""
# Range e operações com range

t = ('dias: ')
r = range(1,5)
print(t+t)
print(r)
print(sorted(r))
print(max(r))
print(len(r))
print("\n\n\n")

for v in r:
    print(v)

print("\n\n\n")

for i in range(1,10,2):
    print(i)

#"""

#"""

# Conjuntos e operações com conjuntos

frutas = {'laranja', 'banana', 'morango', 'uva', 'pera', 'laranja', 'uva', 'abacate'}
print(frutas)
print(type(frutas))
print(sorted(frutas))

a = set('abacate')
b = set('abacaxi')

print(a)
print(b)

print(a-b)
print(a|b)
print(a&b)
print(a^b)

a = set()
b = {}
print(type(a))
print(type(b))

#"""

#"""

# Dicionários e operações com dicionário

pessoa = { 'nome':'João', 'idade':25, 'cidade':'São Paulo' }
print(pessoa)
print(type(pessoa))

#print(pessoa[0]) # ERRO!!
print(pessoa['nome'])
print(pessoa['idade'])

pessoa['país'] = 'Brasil'
print(pessoa)

print(pessoa.keys())
print(pessoa.values())

## Apenas valores IMUTÁVEIS podem ser chave
# dic = {[1,2,3]: 'valor'} # ERRO!!

dicio = {'primeiro': 1, 'segundo':  2, 'terceiro': 3} #simples
dicio_1 = dict(primeiro=1, segundo=2, terceiro=3) #dict
dicio_2 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3])) #primeiro chaves depois valores
dicio_3 = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)]) #Usando Tuplas
dicio_4 = {name: idx + 1 for idx, name in enumerate(('primeiro', 'segundo', 'terceiro'))} #utilizando dict comprehensions
dicio_5 = dict({'primeiro': 1, 'segundo':  2, 'terceiro': 3}) #transformar um dicionario em dicionario

#"""