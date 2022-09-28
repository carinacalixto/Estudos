class Conta:
    
    # Uma conta TEM um cliente
    # Classe cliente existe sem uma conta
    # Isso é uma agregação

    def __init__(self, numero, cliente, saldo, limite=1000.00):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
    
    def extrato(self):
        print("numero: {}\nsaldo: {}".format(self.numero, self.saldo))
    
    def transfere_para(self, destino, valor):
        if(self.saca(valor)):
            destino.deposita(valor)
            return True
        else:
            return False
    
    def toPrint(self):
        print('\n\nconta nro: {}\ntitular: {}\nsaldo: {}\nlimite: {}\n'.format(self.numero, self.titular.nome, self.saldo, self.limite))