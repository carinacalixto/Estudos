# 1) Adicione o modificador de visibilidade privado (dois underscores "__")
# para cada atributo e método da classe Conta.
# 2) Como podemos modificar/ler os atributos e métodos
# privados (dois underscores "__")?
# 3) Modifique o acesso para protegido (um underscore "_") seguindo a convenção do Python.
# Crie métodos de acesso em sua classe Conta atravez do @property
# 4) Tente os comandos na seguinte ordem:
# print(conta._numero), conta._numero = 50, print(conta._numero). O que ocorre?
# 5) Modifique a classe Conta de modo que não seja permitido criar outros atributos
# além dos já definidos utilizando __slots__ 
# 6) Adicione um atributo identificador na classe Conta, esse identificador deve ter um valor
# único para cada instancia de conta. 

import abc
from tributavel import Tributavel
from cliente import Cliente
from historico import Historico

class Conta(abc.ABC):

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', 'identificador']

    _identificador = 0

    def __init__(self, cliente, saldo, limite) -> None:
        Conta._identificador += 1
        #self.identificador = Conta._identificador
        #self._numero = numero
        self._numero = Conta._identificador
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._tipo = "Conta"

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if (valor < 0) :
            print("Saldo NÃO pode ser negativo")
        else:
            self._saldo = valor
    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if (valor<0):
            print("Não há limite negativo")
        else:
            self._limite = valor

    @property
    def historico(self):
        return self._historico

    @property
    def titular(self):
        return self._titular
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, num):
        pass

    def deposita(self,valor) -> bool:
        self._saldo += valor
        self._historico.insere('Depósito de R${}'.format(valor))
        return True
    
    def saca(self,valor) -> bool:
        if( valor <= self._saldo + self._limite ):
            self._saldo -= valor
            self._historico.insere('Saque de R${}'.format(valor))
            return True
        else :
            return False
        
    def extrato(self) -> None:
        print('numero: {}'.format(self._numero))
        print('saldo: {}'.format(self._saldo))
        print('** dados do cliente **')
        print(self._titular.toString())
        self._historico.insere('Efetuou um extrato')
    
    def transfere_para(self, destino, valor) -> bool:
        # self.historico.insere('# Transferência SAÍDA:')
        saque = self.saca(valor)
        # self.historico.insere('#')
        if(saque):
            # destino.historico.insere('# Transferência ENTRADA:')
            destino.deposita(valor)
            # destino.historico.insere('#')
            return True
        else:
            return False

    @abc.abstractmethod
    def atualiza():
        pass
    # def atualiza(self, taxa):
    #     self._saldo += self._saldo * taxa
    #     return self._saldo
        
    def __str__(self) -> str:
        return "Dados da Conta:\nTipo: {}\nNumero: {}\nTitular: {}\nSaldo: {}\nLimite: {}" .format(self._tipo, self._numero, self._titular, self._saldo, self._limite)

class ContaCorrente(Conta):
    
    def __init__(self, cliente, saldo, limite) -> None:
        super().__init__(cliente, saldo, limite)
        self._tipo = 'Conta Corrente'
    
    # Implementação do método abstrato
    def get_valor_imposto(self):
        return self._saldo * 0.01
    
    def atualiza(self, taxa):
        # super().atualiza(taxa*2)
        self._saldo += self._saldo * taxa * 2
        return self._saldo
        
    def deposita(self, valor) -> bool:
        self._saldo += valor #- 0.10 Comentando o trecho da taxa de 0.10 por depósito
        self._historico.insere('Depósito de R${}.\nCobrada taxa de R$0.10'.format(valor))
        return True

class ContaPoupanca(Conta):
    
    def __init__(self, cliente, saldo, limite) -> None:
        super().__init__(cliente, saldo, limite)
        self._tipo = "Conta Poupança"
    
    def atualiza(self, taxa):
        # super().atualiza(taxa*3)
        self._saldo += self._saldo * taxa * 3
        return self._saldo
    
class ContaInvestimento(Conta):
    
    def __init__(self, cliente, saldo, limite) -> None:
        super().__init__(cliente, saldo, limite)
        self._tipo = "Conta Investimento"
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        
    def get_valor_imposto(self):
        return self._saldo * 0.03

if __name__ == '__main__':
    
    c1 = Cliente('João', 'Manoel', '111.111.111-11')
    c2 = Cliente('José', 'Santos', '222.222.222-22')
    c3 = Cliente('Maria', 'Madalena', '333.333.333-33')
    
    
    # conta = Conta(c1, 1000.00, 1500.00)
    cc = ContaCorrente(c2, 100.00, 0)
    
    if (not cc.saca(300.00)):
        print("Saque não efetuado")
    cc.historico.log()
    # cp = ContaPoupanca(c3, 1000.00, 1500)
    # ci = ContaInvestimento(c1, 1000.00, 1500)
    # print(conta.numero)
    # print(conta.titular)
    # print(conta.saldo)
    # print(conta.limite)
    # conta.atualiza(0.01)
    # cc.atualiza(0.01)
    # cp.atualiza(0.01)
    # ci.atualiza(0.01)
    
    # print(conta.saldo)
    # print(cc.saldo)
    # print(cp.saldo)
    # print(ci.saldo)
    
    # print(conta)
    # print(cc)
    # print(cp)
    # print(ci)