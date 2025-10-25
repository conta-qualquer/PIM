class Aula:
    def __init__(self , data , turma , tema):
        self.data = data
        self.turma = turma
        self.tema = tema
    
    def __str__(self) -> str:
       return f'Data da Aula : {self.data} | Turma : {self.turma} | Tema da Aula : {self.tema}'
