from conta import Conta
from cliente import Cliente

# conta = Conta('123-4', 'João', 120.0, 1000.0)

# print(conta.titular)
# print(conta.saldo)

# conta.deposita(20.0)
# conta.extrato()
# if(conta.saca(15)):
#     print("Saque efetivado!")
# else:
#     print("Saque não efetivado!")
# conta.extrato()

# c1 = Conta('127-4', 'Maria', 10.0, 200.0)
# c2 = Conta('136-9', 'Carina', 1500.0, 2000.0)

# print(id(c2))
# print(id(c1))

# print(c2.saldo)
# c2 = c1 # Copia apenas a referencia, dessa forma c1 e c2 apontam para a mesma pos de memoria.
# print(id(c2))
# print(c2.saldo)
# c1.deposita(500)
# print(c2.saldo)

#c3 = Conta('127-4', 'Maria', 10.0, 200.0) # Apesar de ter os msms atributos de c1 a pos de memoria é diferente, logo em teste do if são diferentes.

# if(c1 == c3):
#     print('são iguais')
# else:
#     print('são diferentes')

# c1.transfere_para(c3, 10)
# print(c1.saldo)
# print(c3.saldo)

# c4 = Conta('456-3', 'Ana', 235.00)
# c4.toPrint()

# cliente1 = Cliente('Carina', 'Calixto', '143.140.210-98')
# cliente2 = Cliente('Ana Maria', 'Azevedo', '883.956.700-36')
# cliente3 = Cliente('João', 'Oliveira', '266.982.070-04')

# conta1 = Conta('123-4', cliente1, 1200.00)
# conta2 = Conta('453-9', cliente2, 2000.00)
# conta3 = Conta('978-3', cliente3, 2500.00)

# conta1.deposita(100.0)
# conta1.saca(50.0)
# conta1.transfere_para(conta2, 150.0)
# conta1.extrato()

# conta1.historico.log()