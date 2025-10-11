class Aluno:
    def __init__(self , nome , turma , id):
        self.nome = nome
        self.turma = turma
        self.id = id
    
    def __str__(self):
        return f'Ra : {self.id} | Nome : {self.nome} | Turma : {self.turma}'
