#Aluno: Elias Medeiros

class Node:
    def __init__(self, data=0, next_node = None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return '%s > %s' % (self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)

    def insert(list, new_data):
        new_node = Node(new_data)
        new_node.next = list.head
        list.head = new_node
    
    def pairCount(list):
        head = list.head
        pairs = 0
        while head.next != None:
            rest = head.data % 2
            if(rest == 0):
                pairs = pairs + 1
            head = head.next
        print(f"Quantidade de números pares na lista: {pairs}")
        
    def numberOfSteps(list, value):
        head = list.head
        steps = 1
        while head.next != None:
            if(head.data != int(value)):
                steps = steps + 1
            else:
                print(f'Quantidade de passos para achar o valor {value}: {steps}')
                return
            head = head.next
    
    def verifyOrder(list):
        head = list.head
        previousValue = None
        while head.next != None:
            if(previousValue == None):
                previousValue = head.data
            else:
                if(previousValue > head.data):
                    print("A lista não está em ordem crescente.")
                    return
            head = head.next
        print("A lista está em ordem crescente.")
        
list1 = LinkedList()
for i in range(0, 20, +1):
    list1.insert(i)
    
list2 = LinkedList()
for i in range(10, 0, -1):
    list2.insert(i)

print("/=================================================================/")
print(f'Lista 1: {list1}')
list1.pairCount()
list1.numberOfSteps(9)
list1.verifyOrder()
print("\n/=================================================================/")
print(f'Lista 2: {list2}')
list2.pairCount()
list2.numberOfSteps(9)
list2.verifyOrder()
print("/=================================================================/")
