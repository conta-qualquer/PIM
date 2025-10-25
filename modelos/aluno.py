from string import ascii_letters , digits
from random import choice

class Aluno:
    def __init__(self , nome , turma):
        self.nome = nome
        self.turma = turma
        self.id = self.gerar_id()
        
    
    def __str__(self) -> str:
        return f'Ra : {self.id} | Nome : {self.nome} | Turma : {self.turma}'
    
    def gerar_id(self) -> str:
        caracters = ascii_letters + digits
        ra = ''.join(choice(caracters) for i in range(7))
        return ra
