class Turma:
    def __init__(self , nome , semestre , curso):
        self.nome = nome
        self.semestre = semestre
        self.curso = curso
        
    def __str__(self):
        return 'Turma : {} | Semestre :  {} | Curso : {}'.format(self.nome,self.semestre,self.curso)
