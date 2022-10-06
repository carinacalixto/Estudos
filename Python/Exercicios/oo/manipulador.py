from re import L


class ManipuladorDeTributaveis:
    
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total
    
if __name__ == '__main__':
    from cliente import Cliente
    from conta import ContaCorrente
    from segurodevida import SeguroDeVida
    from tributavel import TributavelMixIn
    
    cliente1 = Cliente('Carina', 'Lopes', '111.111.111-11')
    cliente2 = Cliente('Mariana', 'Gomes', '222.222.222-22')
    
    cc1 = ContaCorrente(cliente1, 1000.00, 500.00)
    cc2 = ContaCorrente(cliente2, 1000.00, 500.00)
    
    seguro1 = SeguroDeVida(100, cliente1, '234243-567')
    seguro2 = SeguroDeVida(200, cliente2, '465343-423')
    
    lista_tributaveis = []
    
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)
    
    manip = ManipuladorDeTributaveis()
    
    total = manip.calcula_impostos(lista_tributaveis)
    
    print(total)