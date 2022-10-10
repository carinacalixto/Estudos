import csv
import os
from typing import MutableSequence
from funcionario import Funcionario

class Funcionarios(MutableSequence):
    
    _dados = []
    
    def __len__(self):
        return len(self._dados)
    
    def __getitem__(self, posicao):
        return self._dados[posicao]
    
    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            self._dados[posicao] = valor
        else:
            raise TypeError('Valor atribuído não é um Funcionario')
    
    def __delitem__(self, posicao):
        del self._dados[posicao]
        
    def insert(self, index, valor):
        if (isinstance(valor, Funcionario)):
            return self._dados.insert(index, valor)
        else:
            raise TypeError('Valor atribuído não é um Funcionario')

if __name__ == '__main__':

    # from diretor import Diretor
    from escriturario import Escriturario

    path = os.getcwd()+'\\Python\\oo\\funcionarios.txt'
    # print(path)
    # funcionarios = []
    funcionarios = Funcionarios()

    try:
        arquivo = open(path, 'r')
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
            func = Escriturario(linha[0], linha[1], linha[2])
            funcionarios.append(func)
    except:
        print("Erro na abertura do arquivo")
    finally:
        arquivo.close()

    # funcionarios[10] = 'Banana'
    # funcionarios.append('Banana')
    print('salário - bonificação')    
    for f in funcionarios:
        print('{} - {}'.format(f.salario, f.get_bonificacao()))