"""_summary_
        Problema do diamante:
         A
        B C
         D
         
         Classe A é "mãe" de B e C.
         Classe D é "filha" de B e C.
         Quais métodos D herda caso tenha métodos com mesmo nome? De B ou de C?
    Returns:
        _type_: _description_
"""
class A:
    def metodo(self):
        print('Método da classe A')

class B(A):
    def metodo(self):
        return super().metodo()
    def outrometodo(self):
        print('Método da classe B')

class C(A):
    def metodo(self):
        return super().metodo()
    def outrometodo(self):
        print("Método da classe C")
    def metodoC(self):
        print("Método existente apenas em C")

class D(B, C):
    # Herda primeiro de B, depois o restante de C
    def metodo(self):
        return super().metodo()
    def outrometodo(self):
        return super().outrometodo()
    def metodoC(self):
        return super().metodoC()

if __name__ == '__main__':
    d = D()
    d.metodo()
    d.outrometodo()
    d.metodoC()