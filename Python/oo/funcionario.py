# Criando uma classe Funcionário com métodos e atributos comuns a todos
# e qualquer tipo de funcionário do nosso sistema.

class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def get_bonificacao(self):
       return self._salario * .10
        
    #outros métodos e propriedades de Funcionario.