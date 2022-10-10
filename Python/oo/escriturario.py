from funcionario import Funcionario


class Escriturario(Funcionario):
    
    def __init__(self, nome, cpf, salario) -> None:
        super().__init__(nome, cpf, salario)
    
    def get_bonificacao(self):
        return super().get_bonificacao()