class Conta:
    
    def __init__(self, numero, titular, saldo, limite=1000.00):
        self.numero = numero
        self.titular = titular
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
        print('\n\nconta nro: {}\ntitular: {}\nsaldo: {}\nlimite: {}\n'.format(self.numero, self.titular, self.saldo, self.limite))