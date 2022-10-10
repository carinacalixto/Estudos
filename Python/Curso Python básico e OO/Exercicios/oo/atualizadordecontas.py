from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca

class AtualizadorDeContas():
    def __init__(self, selic, saldo_total=0) -> None:
        self._selic = selic
        self._saldo_total = saldo_total
    
    # Propriedades
    
    def roda(self, conta):
        try:
            print('Saldo da Conta: {}'. format(conta.saldo))
            self._saldo_total += conta.atualiza(self._selic)
            print('Saldo final da Conta: {}\nSaldo TOTAL: {}'.format(conta.saldo, self._saldo_total))
        except AttributeError as e:
            print(e)
        
if __name__ == '__main__':
    cl1 = Cliente('João', 'Manoel', '111.111.111-11')
    cl2 = Cliente('José', 'Santos', '222.222.222-22')
    cl3 = Cliente('Maria', 'Madalena', '333.333.333-33')
    
    c = Conta(cl1, 1000.00, 1500.00)
    cc = ContaCorrente(cl2, 1000.00, 1500)
    cp = ContaPoupanca(cl3, 1000.00, 1500)
    
    adc = AtualizadorDeContas(0.01)
    
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)
    
    print('Saldo Total: {}'.format(adc._saldo_total))