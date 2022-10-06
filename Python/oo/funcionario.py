# Criando uma classe Funcionário com métodos e atributos comuns a todos
# e qualquer tipo de funcionário do nosso sistema.
import abc

class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario=0):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    @abc.abstractmethod
    def get_bonificacao(self):
       return self._salario * 1.2
        
    #outros métodos e propriedades de Funcionario.
    
# Teste instanciando Funcionario
if __name__ == '__main__':
    # f = Funcionario('Carina', '123.456.789-10', 5000.00) # TypeError: Cant instanciate abstract class...
    pass