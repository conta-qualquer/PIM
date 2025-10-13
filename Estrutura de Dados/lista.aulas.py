class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class ListaAulas:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self , Object_aula):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(Object_aula)
        else:
            self.head = Node(Object_aula)
        self.size += 1
    
    def print_list(self):
        pointer = self.head
        while pointer:
            print(f"{pointer.data}\n")
            pointer = pointer.next
    
    def __len__(self):
        return self.size
    
    def remove(self, aula):
        if aula == self.head.data:
            self.head = self.head.next
        pointer = self.head
        previous = None
        while pointer:
            if pointer.data == aula:
                previous.next = pointer.next
                return
            previous = pointer
            pointer = pointer.next

    def list_(self):
        lista_aulas = []
        pointer = self.head
        while pointer:
            lista_aulas.append(pointer.data)
            pointer = pointer.next
        return lista_aulas
