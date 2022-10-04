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

from historico import Historico

class Conta:

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
