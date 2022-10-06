class Cliente():

    def __init__(self, nome, sobrenome, cpf, senha) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._senha = senha
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso PERMITIDO')
            return True
        else:
            print('Acesso NEGADO')
            return False    