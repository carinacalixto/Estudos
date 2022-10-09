from collections import UserDict


from collections import UserDict
class MeuDicionario(UserDict):
    pass

class Pins(UserDict):
    
    def __contains__(self, key):
        return str(key) in self.keys()
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item
    
if __name__ == '__main__':
    pins = Pins(one = 1)
    print(pins)
    pins[3] = 1
    lista = [1,2,3]
    pins[lista] = 2
    print(pins)