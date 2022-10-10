import datetime

class Historico:

    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def insere(self, mensagem) -> None:
        self.transacoes.append(mensagem)

    def log(self):
        print('** HISTORICO **')
        print('# Data abertura: {}'.format(self.data_abertura))
        print('# Transações: ')
        for t in self.transacoes:
            print('-', t)