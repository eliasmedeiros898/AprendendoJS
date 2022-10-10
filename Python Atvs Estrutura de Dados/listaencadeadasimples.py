#Aluno: Elias Medeiros

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)

        else:
            self.head = Node(element)
        self._size = self._size + 1

    def __len__(self):
        return self._size

    def __getitem__(self,index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self,index, element):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")

    def search(self, element):
        pointer = self.head
        loops = 0
        while(pointer):
            if pointer.data == element:
                return loops
            pointer = pointer.next
            loops += 1
        raise ValueError(f"{element} is not in the list")




