# Criando uma classe Gerente que possua os mesmos métodos e atributos de Funcionário, 
# porém com informações adicionais.

from funcionario import Funcionario

class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados) -> None:
        # Funcionario.__init__(nome, cpf, salario)
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso PERMITIDO')
            return True
        else:
            print('Acesso NEGADO')
            return False

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00
    # Outros métodos comuns a funcionário
    
if __name__ == '__main__':
    g = Gerente('Manoel', '111.111.111-11', 5000.00, '12345', 12)
    print(g.get_bonificacao())