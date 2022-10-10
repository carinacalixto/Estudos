# numero = '123-4'
# titular = 'Carina'
# saldo = 123.65
# limite = 1500.00

# numero2 = '135-7'
# titular2 = 'Mariana'
# saldo2 = 10.05
# limite2 = 1000.00

# conta = {'numero':'123-4', 'titular':'Carina', 'saldo': 123.65, 'limite':1500.00}
# conta2 = {'numero':'135-7', 'titular':'Mariana', 'saldo': 10.05, 'limite':1000.00}
# print('numero => {}'.format(conta['numero']))

def cria_conta(num, tit, saldo, lim):
    conta = {'numero':num, 'titular':tit, 'saldo': saldo, 'limite':lim}
    return conta

# conta3 = cria_conta('234-6', 'Ana Maria', 345.87, 10000.00)
# print('numero => {}'.format(conta3['numero']))

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('número: {}\nsaldo:{}' .format(conta['numero'], conta['saldo']))

conta = cria_conta('123-4', 'João', 120.0, 1000.0)
deposita(conta, 15.0)
extrato(conta)
saca(conta, 20)
extrato(conta)