class Atividade:
    def __init__(self , nome , data , turma):
        self.nome = nome 
        self.data = data
        self.turma = turma
    
    def __str__(self) -> str:
        return f'Nome da Atividade : {self.nome} | Data da Atividade : {self.data} | Turma : {self.turma}'
