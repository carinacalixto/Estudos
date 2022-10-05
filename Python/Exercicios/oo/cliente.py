from mailbox import NotEmptyError


class Cliente:

    def __init__(self, nome, sobrenome, cpf) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __str__(self) -> str:
        return ("\n- Nome: {}\n- Sobrenome: {}\n- cpf: {}"
        .format(self.nome, self.sobrenome, self.cpf))