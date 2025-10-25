class Turma:
    def __init__(self , nome , semestre , curso):
        self.nome = nome
        self.semestre = semestre
        self.curso = curso
        
    def __str__(self) -> str:
        return f'Turma : {self.nome} | Semestre :  {self.semestre} | Curso : {self.curso}'
