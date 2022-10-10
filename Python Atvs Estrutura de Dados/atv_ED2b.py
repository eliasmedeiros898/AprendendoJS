#   Lista - Lista encadeada

#Na classe trabalha-se com índice, ou seja, de 0 a tamanho - 1
#Ao chamar as funções trabalha-se com posições, ou seja, de 1 a tamanho

class Node:
    def __init__(self, elemento, proximo):
        self.elemento = elemento
        self.proximo = proximo

class LinkedList:
    def __init__(self):
        Node.__init__(self, elemento = None, proximo = None)
        self.inicio = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho

    def MOSTRAR(self):
        listaAux = []
        add = None
        aux = self.inicio
        if(aux == None):
            return False
        else:
            while (aux != None):
                add = aux.elemento
                listaAux.append(add)
                aux = aux.proximo
            return listaAux
    
    
    def INSERIR(self, valor, posicao):
        posicao = posicao - 1
        if ((posicao < 0) or (posicao > self.tamanho)):
            print ("Posição inválida!")
            return False
        elif (posicao == 0):
            self.inicio = Node (valor, None)
        else:
            aux = self.inicio
            for i in range (1, posicao):
                aux = aux.proximo
            aux.proximo = Node (valor, aux.proximo)
        self.tamanho = self.tamanho + 1
        return True

    def REMOVER(self, posicao):
        posicao = posicao - 1
        aux = 0
        remover = 0
        if((posicao < 0) or (posicao >self.tamanho)):
            print("Posição inválida!")
            return False
        elif(posicao == 0):
            
            remover = self.inicio
            self.inicio = self.inicio.proximo
            self.tamanho = self.tamanho - 1
            return remover
        else:
            aux = self.inicio
            for i in range(1, posicao):
                aux = aux.proximo
            remover = aux.proximo.elemento
            aux.proximo = aux.proximo.proximo
            self.tamanho = self.tamanho - 1
            return remover
    
 
        
def Comparar(lista1, lista2):
    tamanho1 = lista1.TAMANHO()
    tamanho2 = lista2.TAMANHO()
    if(tamanho1 != tamanho2):
        print("As listas não são iguais.")
        return False
    else:
        aux1 = lista1.inicio
        aux2 = lista2.inicio
        contador = 0
        for i in range(tamanho1):
            if(aux1.elemento != aux2.elemento):
                contador = contador + 1
            aux1 = aux1.proximo
            aux2 = aux2.proximo
        if(contador > 0):
            print("As listas não são iguais.")
            return False
        else:
            print("Listas iguais")
            return True



l1 = LinkedList()
l2 = LinkedList()

l1.INSERIR(4,1)
l1.INSERIR(9,2)
l1.INSERIR(12,3)

l2.INSERIR(5,1)
l2.INSERIR(13,2)
l2.INSERIR(12,3)

l1.MOSTRAR()

Comparar(lista1,lista2)