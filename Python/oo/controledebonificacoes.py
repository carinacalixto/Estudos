from gerente import Gerente
from funcionario import Funcionario

class ControleDeBonificacoes:
    
    def __init__(self, total_bonificacoes=0) -> None:
        self._total_bonificacoes = total_bonificacoes
    
    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()
    
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

if __name__ == '__main__':
    funcionario = Funcionario('João', '111.111.111-11', 2000.00)
    print('Bonificação funcionário: {}' .format(funcionario.get_bonificacao()))
    
    gerente = Gerente('José', '222.222.222-22', 5000.00, '1234', 0)
    print('Bonificação gerente: {}' .format(gerente.get_bonificacao()))
    
    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    
    print('Total: {}' .format(controle.total_bonificacoes))