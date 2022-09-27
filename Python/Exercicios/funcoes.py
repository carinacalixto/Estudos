# 1) Defina uma funcao chamada velocidade_media() que recebe 2 parametros: a distancia percorrida e o tempo gasto

def velocidade_media(dist, temp):
    pass

# 2) Inserir as instruções, ou seja, o que essa função deve fazer.
# Inserir os comandos para calcular a vel média e guardar o resultado em uma variavel 'velocidade'

def velocidade_media(dist, temp):
    velocidade = dist/temp

# 3) Fazer a função imprimir o valor da velocidade média calculada:

def velocidade_media(dist, temp):
    velocidade = dist/temp
    print(velocidade)

# 4) Teste o código com os valores abaixo:
#  - dist = 100 | temp = 20
#  - dist = 125 | temp = 22
#  - dist = 200 | temp = 30 
#  - dist = 50  | temp = 3

velocidade_media(100,20)
velocidade_media(125,22)
velocidade_media(200,30)
velocidade_media(50,3)

# 5) Modifique a função velocidade_media() de modo que ela retorne o resultado calculado

def velocidade_media(dist, temp):
    velocidade = dist/temp
    return velocidade

# 6) Defina uma funcao soma() que recebe dois numeros como parametros e calcula a soma entre eles

def soma(x,y):
    soma = x+y

# 7) Defina uma função subtracao() que recebe dois numeros como parametros e calcula a diferenca entre eles

def subtracao(x,y):
    sub = x-y

# 8) Faça uma função calculadora() que recebe dois numeros como parametros e retorna o resultado da soma e da subtracao entre eles.

def calculadora(x,y):
    return x+y, x-y

# 9) Modifique a função calculadora() e faça ela retornar também o resultado da multiplicação e da divisão dos parametros.

def calculadora(x,y):
    if(y!=0):
        return x+y, x-y, x*y, x/y
    else:
        return x+y, x-y, x*y

# 10) Chame a funcao calculadora() com alguns valores. Ex: 1,2 | 3,4 | 5,0

print(calculadora(2,1))
print(calculadora(4,3))
print(calculadora(5,0))

# 11) (OPCIONAL) Defina uma funcao divisao() que recebe dois numeros como parametros, 
# calcula e retorna o resultado da divisao do primeiro pelo segundo.
# Modifique a funcao velocidade_media() utilizando a funcao divisao() para calcular a velocidade.
# Teste o seu codigo chamando a funcao velocidade_media com os valores abaixo:
#  - dist = 100 | temp = 20
#  - dist = -20 | temp = 10
#  - dist = 150 | temp = 0

def divisao(x,y):
    if (y != 0):
        return x/y
    else:
        return None

def velocidade_media(dist, temp):
    vel = divisao(dist, temp)
    if vel is not None:
        print('Velocidade média: {} m/s'.format(vel))
    else:
        print('Velocidade média: Tende ao infinito')

velocidade_media(100,20)
velocidade_media(-20,10)
velocidade_media(150,0)