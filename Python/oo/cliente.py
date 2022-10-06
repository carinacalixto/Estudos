from autenticavel import Autenticavel

class Cliente(Autenticavel):

    def __init__(self, nome, sobrenome, cpf, senha) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._senha = senha