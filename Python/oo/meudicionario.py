from collections import UserDict

class MeuDicionario(UserDict):
    pass

class Pins(UserDict):
    
    def __contains__(self, key):
        return str(key) in self.keys()
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item
    
    
if __name__ == '__main__':

    from collections import defaultdict, Counter, deque, namedtuple

    # pins = Pins(one = 1)
    # print(pins)
    # pins[3] = 1
    # lista = [1,2,3]
    # pins[lista] = 2
    # print(pins)
    
    # cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]
    # cores_favoritas = defaultdict(list)
    # for chave, valor in cores:
    #     cores_favoritas[chave].append(valor)
    # print(cores_favoritas)
    
    # c = ['amarelo', 'azul', 'azul', 'vermelho', 'azul', 'verde', 'vermelho']
    # contador = Counter(c)
    # print(contador)
    
    # fila = deque()
    # fila.append('1')
    # fila.append('2')
    # fila.append('3')
    # print(len(fila)) # 3
    # print(fila)
    # fila.pop() # removes 3
    # print(fila)
    # fila.append('3')
    # print(fila)
    # fila.popleft() # removes 1 to the left
    # print(fila)
    # fila.appendleft('1') # appends 1 to the left
    # print(fila)
    
    Conta = namedtuple('Conta', 'numero titular saldo limite')
    conta = Conta('123-4', 'João', 1000.00, 1000.00)
    print(conta)
    print(conta.titular)
    # conta.titular = 'José' # Gera AttributeError
    # print(conta.titular)
    print(conta[1]) # imprime Titular