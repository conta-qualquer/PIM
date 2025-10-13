from string import ascii_letters , digits
from random import choice
from aluno import Aluno
from turma import Turma
from lista_alunos import ListaAlunos
from lista_turmas import ListaTurma
from lista_aulas import ListaAulas
from registro_aula import RegistroAula
from atividade import Atividade
from menus  import *


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
 
def registro_aula():
    print("\n------------Registro de Aula--------------")
    dia = str(input("\nDigite a data da Aula: "))
    tema = str(input("Digite o tema da Aula: "))
    turma = str(input("Digite a Turma: "))  
    return RegistroAula(dia,turma,tema)
    
def cadastro_atividade():
    nome = str(input("\nDigite o nome da atividade: ")).strip()
    tipo = str(input("Digite o tipo da aitvidade: ")).strip()
    prazo = str(input("Digite o prazo da Atividade: ")).strip()
    dificuldade = str(input("Digite a Dificuladade da Atividade: ")).strip()

def continuar():
        op = str(input("Deseja voltar para o menu principal ? :  [S/N]")).lower().strip()
        if op == 'n':
             return op == 'n'

alunos_list = ListaAlunos()
turma_list = ListaTurma()
aula_list = ListaAulas()

while True:
    
    menu_principal()

    try:
        op = str(input("\nDigite uma das opção acima: "))
    except ValueError:
        print("Insira um dos valores Acima")

    if op == '1':
        menu_aluno()
        verificar = False
        if (op1 := str(input("\nDigite umas das opções acima: ").strip())) == '1':
            aluno_novo = cadastro_aluno()
            for turma in turma_list.list_():
                if turma.nome == aluno_novo.turma:
                    alunos_list.append(aluno_novo)
                    print("\nCadastro do aluno(a) {} feito com sucesso ✅!!".format(aluno_novo.nome))
                    print("RA do Aluno(a) {} é : {}\n".format(aluno_novo.nome,aluno_novo.id))
                    verificar = True
                    break
            if not verificar:
                print("\n😔Não foi possivel fazer o cadastro do aluno pois esta turma não existe!!")
                print("Cadastre uma turma primeiro para poder cadastrar alunos\n")
                 
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
    elif op == '3':
        if 0 == len(turma_list):
            print("\nNão existe Turmas no Sistema!!\n")
        else:
            menu_aulas()
            if (op1 := str(input("\nDigite uma das opções acima: ")).strip()) == '1':
                aula_nova = registro_aula()
                aula_list.append(aula_nova)
                print("\nAula cadastrada com sucesso✅!!\n")
            elif op1 == '2':
                buscar = str(input("\nDigite o nome da turma para saber suas aulas: ")).strip()
                if 0 == len(aula_list):
                    print(f"\nNão existe nenhuma turma no sistema!")
                else:
                    print("\n----------Aulas da Turma {}----------".format(buscar))
                    verificar = False
                    for aulas in aula_list.list_():
                        if aulas.turma == buscar:
                            print(f"\nData da Aula : {aulas.data} | Tema da Aula{aulas.tema}\n")
                            verificar = True
                    if not verificar:
                        print("\nTurma não Encontrada!!\n")
            elif op1 == '3':
                buscar = str(input("\nDigite a data da aula para consulta-lá: ")).strip()
                verificar = False
                print("------------Aulas da Turma {}--------------".format(buscar))
                for aulas in aula_list.list_():
                    if buscar == aulas.data:
                        print(f"\nData da Aula : {aulas.data} | Tema da Aula : {aulas.tema}\n")
                        verificar = True
                if not verificar:
                    print("\nTurma não Encontrada no Sistema!!\n")

    if continuar():
        print("\nPROGRAMA ENCERRADO\n")
        break
