# Criando uma classe Funcionário com métodos e atributos comuns a todos
# e qualquer tipo de funcionário do nosso sistema.
import abc
from msilib.schema import Property

class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario=0):
        self._nome = nome
        self._cpf = cpf
        self._salario = float(salario)
    
    @property
    def salario(self):
        return self._salario
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @abc.abstractmethod
    def get_bonificacao(self):
       return self._salario * 1.2
        
    #outros métodos e propriedades de Funcionario.
    
# Teste instanciando Funcionario
if __name__ == '__main__':
    # f = Funcionario('Carina', '123.456.789-10', 5000.00) # TypeError: Cant instanciate abstract class...
    pass