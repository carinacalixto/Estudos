import datetime

class Historico:

    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def log(self):
        print('data abertura: {}'.format(self.data_abertura))
        print('transações: ')
        for t in self.transacoes:
            print('-', t)