from historico import Historico

class Conta:
    def __init__(self, numero, cliente, saldo, limite) -> None:
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def deposita(self,valor) -> bool:
        self.saldo += valor
        self.historico.insere('Depósito de R${}'.format(valor))
        return True
    
    def saca(self,valor) -> bool:
        if valor <= self.saldo + self.limite :
            self.saldo -= valor
            self.historico.insere('Saque de R${}'.format(valor))
            return True
        else :
            return False
        
    def extrato(self) -> None:
        print('numero: {}'.format(self.numero))
        print('saldo: {}'.format(self.saldo))
        print('** dados do cliente **')
        print(self.titular.toString())
        self.historico.insere('Efetuou um extrato')
    
    def transfere_para(self, destino, valor) -> bool:
        # self.historico.insere('# Transferência SAÍDA:')
        saque = self.saca(valor)
        # self.historico.insere('#')
        if(saque):
            # destino.historico.insere('# Transferência ENTRADA:')
            destino.deposita(valor)
            # destino.historico.insere('#')
            return True
        else:
            return False
