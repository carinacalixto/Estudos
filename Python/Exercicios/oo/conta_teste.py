from cliente import Cliente
from conta import Conta


cliente1 = Cliente('Carina', 'Azevedo', '899.351.290-63')
cliente2 = Cliente('Victor', 'Pereira', '580.294.760-86')
conta1 = Conta('123-4', cliente1, 1500.00, 1000.00)
conta2 = Conta('353-5', cliente2, 500.00, 1000.00)
# print(type(conta))

# print(conta.numero)
# print(conta.titular)

conta1.deposita(50)
# conta1.extrato()
conta1.saca(20)
# conta1.extrato()
conta1.transfere_para(conta2, 500)
conta1.transfere_para(conta2, 50)
# conta1.extrato()
conta2.transfere_para(conta1, 250)

conta1.historico.log()

# conta2.extrato()
conta2.historico.log()