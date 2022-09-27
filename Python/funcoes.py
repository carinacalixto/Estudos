def diz_oi():
    print('oi')

def velocidade_return(esp, temp):
    return (esp/temp)

def velocidade(esp, temp):
    v = esp/temp
    print('Velocidade: {}m/s' .format(v))

def dados(nome, idade=None):
    print('nome: {}' .format(nome))
    if (idade is not None):
        print('idade: {}'.format(idade))
    else:
        print('idade: Não informada')

def dados_return(nome, idade=None):
    if (idade is not None):
        return ('nome: {}\nidade: {}'.format(nome,idade))
    else:
        return ('nome: {}\nidade: Não informada'.format(nome))

def calculadora(x, y):
    return x+y, x-y

def calculadora_dic(x, y):
    return {'soma':x+y, 'subtracao':x-y}

diz_oi()
velocidade(100,20)
dados('Carina', 36)
dados('Victor')

dados(25) # 25 será considerado o nome e não haverá idade informada
# dados(,44) # ERRO!! O primeiro parâmetro precisa ser informado.

print(velocidade_return(450,80))
aceleracao = velocidade_return(450,80)/20
print('{}m/s²'.format(aceleracao))

print(dados_return('Fátima', 55))
print(dados_return('José'))

print(calculadora(3,5))
print(type(calculadora(3,5)))

calc_res = calculadora_dic(73, 24)
for key in calc_res:
    print('{} : {}' .format(key,calc_res[key]))