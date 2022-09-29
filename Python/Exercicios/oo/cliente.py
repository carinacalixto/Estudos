from mailbox import NotEmptyError


class Cliente:

    def __init__(self, nome, sobrenome, cpf) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def toString(self) -> str:
        s = '- Nome: '+self.nome+'\n- Sobrenome: '+self.sobrenome+'\n- cpf: '+self.cpf+'\n'
        return s