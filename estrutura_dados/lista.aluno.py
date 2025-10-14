class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class ListaAlunos:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self , Object_aluno):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(Object_aluno)
        else:
            self.head = Node(Object_aluno)
        self.size += 1
    
    def print_list(self):
        pointer = self.head
        while pointer:
            print(f"{pointer.data}\n")
            pointer = pointer.next
    
    def __len__(self):
        return self.size
    
    def remove(self, aluno):
        if aluno == self.head.data:
            self.head = self.head.next
        pointer = self.head
        previous = None
        while pointer:
            if pointer.data == aluno:
                previous.next = pointer.next
                return
            previous = pointer
            pointer = pointer.next
        self.size -= 1

    def list_(self):
        lista_alunos = []
        pointer = self.head
        while pointer:
            lista_alunos.append(pointer.data)
            pointer = pointer.next
        return lista_alunos
