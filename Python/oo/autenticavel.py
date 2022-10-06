class Autenticavel:
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso PERMITIDO')
            return True
        else:
            print('Acesso NEGADO')
            return False