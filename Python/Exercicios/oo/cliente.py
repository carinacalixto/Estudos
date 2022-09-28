from mailbox import NotEmptyError


class Cliente:

    def __init__(self, nome, sobrenome, cpf) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    
