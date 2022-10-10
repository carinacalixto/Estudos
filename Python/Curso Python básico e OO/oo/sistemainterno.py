from cliente import Cliente
from gerente import Gerente
from diretor import Diretor
from autenticavel import Autenticavel


class SistemaInterno():
    
    def login(self, obj, senha) -> bool:
        if(isinstance(obj, Autenticavel)):
            obj.autentica(senha)
            return True
        else:
            print("{} não é autenticável".format(obj.__class__.__name__))
            return False
        
if __name__ == '__main__':
    
    # obriga as classes a implementar metodos
    Autenticavel.register(Diretor)
    Autenticavel.register(Gerente)
    Autenticavel.register(Cliente)
    
    d = Diretor('Maria', '222.222.222-22', 7000.00, '12345')
    g = Gerente('Manoel', '111.111.111-11', 5000.00, '12345', 12)
    c = Cliente('Victor', 'de Souza', '333.333.333-33', '12345')

    sist = SistemaInterno()
    sist.login(d, '12345')
    sist.login(g, '54321')
    sist.login(c, '12345')
    