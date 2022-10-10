from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca
from atualizadordecontas import AtualizadorDeContas

class Banco:
    
    def __init__(self) -> None:
        self._contas = []
    
    # def __init__(self, conta) -> None:
    #     self._contas = [conta]
    
    @property
    def contas(self):
        return self._contas
    
    def adiciona(self, conta):
        self._contas.append(conta)
    
    def pegaConta(self, id):
        return self._contas[id]
    
    def pegaTotalDeContas(self) -> int:
        return len(self._contas)
    
if __name__ == '__main__':
    bb = Banco()
    
    c1 = Cliente('João', 'Manoel', '111.111.111-11')
    c2 = Cliente('José', 'Santos', '222.222.222-22')
    c3 = Cliente('Maria', 'Madalena', '333.333.333-33')
    c = Conta(c1, 1000.00, 1500.00)
    cc = ContaCorrente(c2, 1000.00, 1500)
    cp = ContaPoupanca(c3, 1000.00, 1500)
    
    bb.adiciona(c)
    bb.adiciona(cc)
    bb.adiciona(cp)
    
    atualContas = AtualizadorDeContas(0.01)
    
    for conta in bb.contas:
        atualContas.roda(conta)
        
    # Teste de excessão ex. 5
    atualContas.roda('Bola')