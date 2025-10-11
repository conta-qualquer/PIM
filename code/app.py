from string import ascii_letters , digits
from random import choice
from aluno import Aluno
from turma import Turma
from lista_alunos import LISTALUNOS
from lista_turmas import LISTATURMA
from registro_aula import RegistroAula
from atividade import Atividade

def menu_principal():
    print("\n\n------------Bem Vindo ao Menu Principal------------")
    print("\n1-Gerenciar Alunos")
    print("2-Gerenciar Turmas")
    print("3-Gerenciar Aulas")
    print("4-Gerenciar Atividades")
    print("5-Inteligencia Artificial")
    print("6-Relatorios e Consultas")
    print("7-sair")

def menu_aluno():
    print("\n----------GERENCIAR ALUNO----------")
    print("\n1-Cadastrar Aluno")
    print("2-Listar Alunos")
    print("3-Buscar Aluno")

def menu_turma():
    print("\n----------GERENCIAR TURMA----------")
    print("\n1-Cadastrar Turma")
    print("2-Listar Turmas")
    print("3-Ver alunos da Turma")

def menu_aulas():
    print("\n----------GERENCIAR AULAS----------")
    print("\n1-Registrar Aulas")
    print("2-Listar Aulas de uma Turma")
    print("3-Consulta aulas por Data")

def menu_atividade():
    print("\n----------GERENCIAR ATIVIDADE----------")
    print("\n1-Cadastrar Atividade")    
    print("2-Listar Atividade")    
    print("3-Consulta Atividade por Turma")

def id_generator():
    caracters = ascii_letters + digits
    return ''.join(choice(caracters) for i in range(7))   

def cadastro_aluno():
    print("\n----------CADASTRO ALUNO----------")
    nome = str(input("\nDigite o nome do aluno(a): ")).strip()
    turma = str(input("Digite o nome da turma aluno(a): ")).strip()
    Id = id_generator()
    return Aluno(nome,turma,Id)
       
def cadastro_turma():
    print("\n----------CADASTRO TURMA----------")
    nome = str(input("\nDigite o nome da turma: ")).strip()
    semestre = str(input("Digite o semestre da turma: ")).strip()
    curso = str(input("Digite o curso da turma: ")).strip()
    return Turma(nome,semestre,curso)
 
def registro():
    dia = str(input("\nDigite a data da Aula: "))
    tema = str(input("Digite o tema da Aula: "))
    turma = str(input("Digite a Turma: "))  
    
def cadastro_atividade():
    nome = str(input("\nDigite o nome da atividade: ")).strip()
    tipo = str(input("Digite o tipo da aitvidade: ")).strip()
    prazo = str(input("Digite o prazo da Atividade: ")).strip()
    dificuldade = str(input("Digite a Dificuladade da Atividade: ")).strip()

alunos_list = LISTALUNOS()
turma_list = LISTATURMA()

while True:

    def continuar():
        op = str(input("Deseja voltar para o menu principal ? :  [S/N]")).lower().strip()
        if op == 'n':
             return op == 'n'
    
    menu_principal()

    try:
        op = str(input("\nDigite uma das opção acima: "))
    except ValueError:
        print("Insira um dos valores Acima")

    if op == '1':
        menu_aluno()
        if (op1 := str(input("\nDigite umas das opções acima: ").strip())) == '1':
            aluno_novo = cadastro_aluno()
            alunos_list.append(aluno_novo)
            print("\nCadastro do aluno(a) {} feito com sucesso ✅!!".format(aluno_novo.nome))
            print("RA do Aluno(a) {} é : {}\n".format(aluno_novo.nome,aluno_novo.id))
        elif op1 == '2':
            print("\n----------Alunos Cadastrados no Sistema----------\n")
            if 0 == len(alunos_list):
                print("\nNÃO HÁ ALUNOS CADASTRADOS NO SISTEMA!\n")
            else:
                alunos_list.print_list()
        elif op1 == '3':
            buscar = str(input('\nDigite o RA do aluno que deseja buscar: ')).strip()
            if 0 == len(alunos_list):
                print("\nNÃO HÁ ALUNOS CADASTRADOS NO SISTEMA!\n")
            else:
                for aluno in alunos_list.list_():
                    if buscar == aluno.id:
                        print('\n------------ALUNO ENCONTRADO COM SUCESSO--------------\n')
                        print('{}\n'.format(aluno))
                    else:
                        print("\nEste RA não existe no Sistema!\n")
        else:
            print("\nERRO! VALOR INVÁLIDO!!\n")
            
    elif op == '2':
        menu_turma()
        if (op1 := str(input("\nDigite um das opões acima: ").strip())) == '1':
            turma_nova = cadastro_turma()
            turma_list.append(turma_nova)
            print("\nTurma Cadastrada com Sucesso ✅!!\n")
        elif op1 == '2':
            if 0 == len(turma_list):
                print("\nNÃO HÁ TURMAS CADASTRADAS NO SISTEMA!!\n")
            else:
                turma_list.print_list()
        elif op1 == '3':
            if 0 == len(turma_list):
                print("\nNÃO HÁ TURMAS CADASTRADAS!!\n")
            else:
                buscar = str(input("\nDigite o nome da Turma: ")).strip()
                print("\n----------ALUNOS NA TURMA {}----------\n".format(buscar))
                for aluno in alunos_list.list_():
                    if aluno.turma == buscar:
                        print(f"\n-{aluno.nome}\n")
                    else:
                        print("\nTURMA NÃO ENCONTRADA NO SISTEMA!!\n")
    if continuar():
        print("\nPROGRAMA ENCERRADO\n")
        break
