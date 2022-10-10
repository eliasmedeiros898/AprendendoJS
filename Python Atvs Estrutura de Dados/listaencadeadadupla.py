#Aluno: Elias Medeiros

from ctypes import pointer


class Node:

    def __init__(self, init_data, prev, next):
        self.data = init_data
        self.prev = prev
        self.next = next

    def getData(self):
        return self.data
    
    def setData(self, element):
        self.data = element


class DoubleLinkedList():

    def __init__(self):
        self.head = Node(None,None,None)
        self.trailer = Node(None,None,None)
        self.head.next = self.trailer
        self.trailer.prev = self.head
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size


    def lowestData(self):
        lowest = self.head
        pointer = self.head
        while(pointer):
            if pointer.data > lowest.data:
                lowest.data = pointer.data
        return lowest.data