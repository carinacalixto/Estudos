# Criando uma classe Gerente que possua os mesmos métodos e atributos de Funcionário, 
# porém com informações adicionais.

class Gerente:
    
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso PERMITIDO')
            return True
        else:
            print('Acesso NEGADO')
            return False

    # Outros métodos comuns a funcionário