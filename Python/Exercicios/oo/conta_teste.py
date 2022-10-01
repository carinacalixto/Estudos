from cliente import Cliente
from conta import Conta


cliente1 = Cliente('Carina', 'Azevedo', '899.351.290-63')
cliente2 = Cliente('Victor', 'Pereira', '580.294.760-86')
conta1 = Conta(cliente1, 1500.00, 1000.00)
conta2 = Conta(cliente2, 500.00, 1000.00)
# print(type(conta))

# print(conta1._numero)
# conta1._numero = 3
# print(conta1._numero)
# print(conta.titular)

# print(conta1.identificador)
# print("Atributo de CLASSE: ", Conta._identificador)
# print(conta2.identificador)
# print("Atributo de CLASSE: ", Conta._identificador)

# conta1.deposita(50)
conta1.extrato()
# conta1.saca(20)
conta2.extrato()
# conta1.transfere_para(conta2, 500)
# conta1.transfere_para(conta2, 50)
# conta1.extrato()
# conta2.transfere_para(conta1, 250)

# conta1.historico.log()

# conta2.extrato()
# conta2.historico.log()