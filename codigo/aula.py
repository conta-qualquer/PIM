class Aula:
    def __init__(self , data , turma , tema):
        self.data = data
        self.turma = turma
        self.tema = tema
    
    def __str__(self) -> str:
       return 'Data da Aula : {} | Turma : {} | Tema da Aula : {}'.format(self.data,self.turma,self.tema)
