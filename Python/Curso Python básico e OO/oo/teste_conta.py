"""
    Este módulo contem funções para criação e manipulação de contas.
"""

def cria_conta(numero, titular, saldo, limite):
    """
        Essa função cria uma conta contendo número, titular, saldo e limite
    """
    conta = {'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta

def deposita(conta, valor):
    """
        Essa função realiza o depósito na conta.
    """
    conta['saldo'] += valor

def saca(conta, valor):
    """
        Essa função realiza o saque na conta.
    """
    conta['saldo'] -= valor

def extrato(conta):
    """
        Essa função realiza a operação de extrato.
    """
    print('* numero: {}\n* saldo: {}'.format(conta['numero'], conta['saldo']))

if __name__ == "__main__":
    conta = cria_conta('123-7', 'João', 500.0, 1000.0)
    deposita(conta, 50.0)
    extrato(conta)
    # saldo 550.0
    saca(conta, 20.0)
    extrato(conta)
    # saldo 530.0