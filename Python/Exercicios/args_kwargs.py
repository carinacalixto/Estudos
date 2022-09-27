# 1) Crie um arquivo com uma função chamada teste_args_kwargs() que recebe três argumentos e imprime cada um deles
print('\n****** Exercício 1 ******\n')
def teste_args_kwargs(arg1, arg2, arg3):
     print('Primeiro argumento:', arg1)
     print('Segundo argumento:', arg2)
     print('Terceiro argumento:', arg3)

teste_args_kwargs('Me', 'Chamo', 'Carina')

# 2) Chamar a função utilizando *args (tupla ou lista)
print('\n****** Exercício 2 ******\n')
args = ('Me', 'chamo', 'Carina')
args2 = ['Tenho', 36, 'anos']
teste_args_kwargs(*args)
teste_args_kwargs(*args2)

# 3) Teste a mesma função utilizando **kwargs. Para isto, crie um dicionário com 3 argumentos (arg1, arg2, arg3)
print('\n****** Exercício 3 ******\n')
kwargs = {'arg1':'Carina', 'arg3':36, 'arg2':1.60}
teste_args_kwargs(**kwargs)

# 4) (OPCIONAL) Tente chamar a mesma função, mas adicionandclso um quarto argumento na variável args e kwargs dos exercicios anteriores.
# O que acontece se a função recebe mais de 3 argumentos?
print('\n****** Exercício 4 ******\n')
args3 = ('Meu', 'nome', 'é', 'Carina')
kwargs2 = {'arg1':'Carina', 'arg3':36, 'arg2':1.60, 'arg4':'Goiânia'}
# teste_args_kwargs(**kwargs2) # ERRO! Recebeu um argumento inesperado 'arg4'
# teste_args_kwargs(*args3) # ERRO! A função recebe 3 arumentos, mas foram dados 4

# 5) Como resolver o problema do exercício anterior?
print('\n****** Exercício 5 ******\n')
def teste_args_kwargs(*args,**kwargs):
    if (args is not None):
        pos = 1
        for a in args:
            print('Argumento #{}: {}' .format(pos,a))
            pos += 1
    if(kwargs is not None):
        for k,a in kwargs.items():
            print('Argumento {} => {}'.format(k, a))

teste_args_kwargs(**kwargs2)
teste_args_kwargs(*args3)