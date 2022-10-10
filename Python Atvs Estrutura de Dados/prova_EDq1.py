from mimetypes import init


class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None
    

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def vazia(self):
        if self.inicio is None:
            return True
        return False
    def concatenar(self, l1, l2):
        
        
    
    #def addInicio(self, valor):
    #    no = Node(valor)
    #    if self.vazia():
    #        self.inicio = self.fim = no
    #    else:
    #        no.proximo = self.inicio
    #        self.inicio.anterior = no
    #        no.anterior = None
    #        self.inicio = no
    
   # def addFim(self,valor):
   #     no = Node(valor)
   #     if self.vazia():
   #         self.inicio = self.fim = no
   #     else:
   #         self.fim.proximo = no
   #         no.anterior = self.fim
   #         no.proximo = None
   #         self.fim = no

    




    




