class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class ListaAtividade:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self , Object_atividade):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(Object_atividade)
        else:
            self.head = Node(Object_atividade)
        self.size += 1
    
    def print_list(self):
        pointer = self.head
        while pointer:
            print(f"{pointer.data}\n")
            pointer = pointer.next
    
    def __len__(self):
        return self.size
    
    def remove(self, atividade):
        if atividade == self.head.data:
            self.head = self.head.next
        pointer = self.head
        previous = None
        while pointer:
            if pointer.data == atividade:
                previous.next = pointer.next
                return
            previous = pointer
            pointer = pointer.next
        self.size -= 1
        
    def to_list(self):
        lista_atividade = []
        pointer = self.head
        while pointer:
            lista_atividade.append(pointer.data)
            pointer = pointer.next
        return lista_atividade
