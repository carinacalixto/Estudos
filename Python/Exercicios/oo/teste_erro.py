from cliente import Cliente
from conta import ContaCorrente

def metodo1():
    print("Inicio do método 1")
    metodo2()
    # try:
    #     metodo2()
    # except:
    #     print("Erro na chamada de método 2")
    print("Fim do método 1")

def metodo2():
    print("Inicio do método 2")
    cliente = Cliente('Cristina', 'Freitas', '555.555.555-55')
    cc = ContaCorrente(cliente, 0, 0)
    # for i in range(1,15):
    #     cc.deposita(i+1000)
    #     print(cc.saldo)
    #     if(i==5):
    #         cc = None
    # try:
    #     for i in range(1,15):
    #         cc.deposita(i+1000)
    #         print(cc.saldo)
    #         if(i==5):
    #             cc = None
    # except:
    #     print("\nERRO\n")
    
    for i in range(1,15):
        try:
            cc.deposita(i+1000)
            print(cc.saldo)
            if(i==5):
                cc = None
        except:
            print("ERRO")
    print("Fim do método 2")
    
if __name__ == '__main__':
    print('inicio de main')
    metodo1()
    # try:
    #     metodo1()
    # except:
    #     print("\nERRO na chamada de método 1")
    print('fim do main')