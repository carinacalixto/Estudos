from historico import Historico

class Conta:
    
    # Uma conta TEM um cliente
    # Classe cliente existe sem uma conta
    # Isso é uma agregação

    _total_contas = 0

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo=0.00, limite=1000.00):
        Conta._total_contas += 1
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()

    @classmethod
    def get_total_contas(cls):
        return Conta._total_contas

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if(valor < 0):
            print('Saldo não pode ser negativo')
        else:
            self._saldo = valor

    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))

    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True
    
    def extrato(self):
        print("numero: {}\nsaldo: {}".format(self.numero, self._saldo))
        self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self._saldo))
    
    def transfere_para(self, destino, valor):
        if(self.saca(valor)):
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia de {} para a conta {}".format(valor, destino.numero))
            return True
        else:
            return False
    
    def toPrint(self):
        print('\n\nconta nro: {}\ntitular: {}\nsaldo: {}\nlimite: {}\n'.format(self.numero, self.titular.nome, self._saldo, self.limite))