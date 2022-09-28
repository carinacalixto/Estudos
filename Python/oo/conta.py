from historico import Historico

class Conta:
    
    # Uma conta TEM um cliente
    # Classe cliente existe sem uma conta
    # Isso é uma agregação

    def __init__(self, numero, cliente, saldo, limite=1000.00):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True
    
    def extrato(self):
        print("numero: {}\nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self.saldo))
    
    def transfere_para(self, destino, valor):
        if(self.saca(valor)):
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia de {} para a conta {}".format(valor, destino.numero))
            return True
        else:
            return False
    
    def toPrint(self):
        print('\n\nconta nro: {}\ntitular: {}\nsaldo: {}\nlimite: {}\n'.format(self.numero, self.titular.nome, self.saldo, self.limite))