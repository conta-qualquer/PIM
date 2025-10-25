from aluno import *
from turma import *
from atividade import *
from aula import *

def cadastro_aluno():
    print("\n----------CADASTRO ALUNO----------")
    nome = str(input("\nDigite o nome do aluno(a): ")).strip()
    turma = str(input("Digite o nome da turma aluno(a): ")).strip()
    return Aluno(nome,turma)
       
def cadastro_turma():
    print("\n----------CADASTRO TURMA----------")
    nome = str(input("\nDigite o nome da turma: ")).strip()
    semestre = str(input("Digite o semestre da turma: ")).strip()
    curso = str(input("Digite o curso da turma: ")).strip()
    return Turma(nome,semestre,curso)
 
def registro_aula():
    print("\n------------Registro de Aula--------------")
    dia = str(input("\nDigite a data da Aula: "))
    tema = str(input("Digite o tema da Aula: "))
    turma = str(input("Digite a Turma: "))  
    return Aula(dia,turma,tema)
    
def cadastro_atividade():
    nome = str(input("\nDigite o nome da atividade: ")).strip()
    data = str(input("Digite a data da atividade: ")).strip()
    turma = str(input("Digite o nome da turma que será realizada a atividade: ")).strip()
    return Atividade(nome,data,turma)
