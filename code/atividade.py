class Atividade():
    def __init__(self ,nome,data,turma):
        self.nome = nome
        self.data = data
        self.turma = turma
    
    def __str__(self) -> str:
        return 'Nome da Atividade : {} | Data da Atividade : {} | Turma : {}'.format(self.nome,self.data,self.turma)
