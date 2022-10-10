class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
            
    
    def minimumNode(self):
        current = self.head
        if(self.head == None):
            print("Lista vazia")
            return 0
        else:
            min = self.head.data
            while(current != None):
                if(min > current.data):
                    min = current.data
                current = current.next
        return min

    
    def dataHeight(self,data):
        pointer = self.tail
        cont = 0
        while(pointer):
            if(pointer.data == data):
                cont+=1
                return cont
            else:
                cont+=1
                pointer = self.tail.previous
        

dList = DoublyLinkedList()

dList.addNode(5)
dList.addNode(7)
dList.addNode(9)
dList.addNode(1)
dList.addNode(2)

value = 7

print("O menor valor da lista é: "+ str(dList.minimumNode()))

print(f"A altura do valor {value} é: " + str(dList.dataHeight(value)))
