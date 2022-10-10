from tributavel import Tributavel

class SeguroDeVida():
    def __init__(self, valor, cliente, numero_apolice) -> None:
        self._valor = valor
        self._titular = cliente
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05