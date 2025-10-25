class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class ListaTurma:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self , Object_turma):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(Object_turma)
        else:
            self.head = Node(Object_turma)
        self.size += 1
    
    def print_list(self):
        pointer = self.head
        while pointer:
            print(f"{pointer.data}\n")
            pointer = pointer.next
    
    def __len__(self):
        return self.size
    
    def remove(self, turma):
        if turma == self.head.data:
            self.head = self.head.next
        pointer = self.head
        previous = None
        while pointer:
            if pointer.data == turma:
                previous.next = pointer.next
                return
            previous = pointer
            pointer = pointer.next
        self.size -= 1
        

    def to_list(self):
        lista_turma_geral = []
        pointer = self.head
        while pointer:
            lista_turma_geral.append(pointer.data)
            pointer = pointer.next
        return lista_turma_geral
