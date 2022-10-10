def teste(arg, *args):
    print('Meu primeiro argumento normal: {}' .format(arg))
    for a in args:
        print('Outro argumento: {}' .format(a))

def teste2(**kwargs):
    for k,a in kwargs.items():
        print('{} => {}' .format(k,a))

def teste3(*args,**kwargs):
    for a in args:
        print('Outro argumento: {}' .format(a))
    for k,a in kwargs.items():
        print('{} => {}' .format(k,a))

teste('Estudar', 'Python', 'é', 'muito', 'interessante', '!')


lista = ['vários', 'elementos', 'em', 'uma', 'lista']
teste('Imprimir', *lista)

tupla = ('são', 'elementos', 'de', 'uma', 'tupla')
teste('Parâmetros', *tupla)
teste3(*tupla)

dic = {'nome':'Carina', 'idade':'36', 'cidade':'Goiânia'}
teste('Pessoa', *dic)
teste2(**dic)
teste3(**dic)
