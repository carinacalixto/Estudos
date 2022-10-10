from excecoes import SaldoInsuficienteError

class CaixaEletronico:
    def __init__(self) -> None:
        pass
    
    def deposito(self, conta, valor):
        try:
            conta.deposita(valor)
            print("Depósito de {} realizado com sucesso.".format(valor))
        except ValueError:
            print("O valor a ser depositado deve ser um número positivo.")
            
    def saque(self, conta, valor):
        try:
            conta.saca(valor)
            print("Saque de {} realizado com sucesso.".format(valor))
        except ValueError:
            print("O valor a ser sacado deve ser um número positivo.")
        except SaldoInsuficienteError:
            print("Saldo insuficiente.")
            
if __name__ == '__main__':
    
    from cliente import Cliente
    from conta import ContaCorrente, Conta, ContaInvestimento, ContaPoupanca
    
    caixa = CaixaEletronico()
    
    c1 = Cliente('João', 'Manoel', '111.111.111-11')
    c2 = Cliente('José', 'Santos', '222.222.222-22')
    c3 = Cliente('Maria', 'Madalena', '333.333.333-33')
    
    cc = ContaCorrente(c2, 1000.00, 0)
    
    caixa.deposito(cc,-100)
    caixa.saque(cc,-100)
    caixa.deposito(cc,1000)
    caixa.saque(cc,1000)
    caixa.saque(cc,5000)
    