from funcionario import Funcionario

class Diretor(Funcionario):
    
    def __init__(self, nome, cpf, salario=0):
        super().__init__(nome, cpf, salario)
    
    def get_bonificacao(self):
        return super().get_bonificacao() + 2000.00
    
if __name__ == '__main__':
    # Como não implementa get_bonificacao, ainda é considerada abstrata!
    d = Diretor('Maria', '222.222.222-22', 7000.00) # TypeError: Cant instantiate abstract class Diretor...
    print(d.get_bonificacao())