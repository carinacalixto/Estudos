import abc

class Tributavel(abc.ABC):
    """Classe que contém operações de um objeto autenticável
       As subclasses concretas devem sobreescrever o método get_valor_imposto

    Args:
        abc ():
    """
    
    @abc.abstractmethod
    def get_valor_imposto(self):
        """Aplica taxa de imposto sobr um determinado valor do objeto
        """
        pass
if __name__ == '__main__':
    help(Tributavel)