from string import ascii_letters , digits
from random import choice
from aluno import Aluno
from turma import Turma
from atividade import Atividade
from registro_aula import RegistroAula
from lista_alunos import ListaAlunos
from lista_turmas import ListaTurma
from lista_aulas import ListaAulas
from lista_atividades import ListaAtividade
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
    data = str(input("Digite a data da atividade: ")).strip()
    turma = str(input("Digite o nome da turma que será realizada a atividade: ")).strip()
    return Atividade(nome,data,turma)

def continuar():
        op = str(input("Deseja voltar para o menu principal ? :  [S/N]")).lower().strip()
        if op == 'n':
             return op == 'n'

def verificar_vazio(lista):
        return True if len(lista) == 0 else False

alunos_list = ListaAlunos()
turma_list = ListaTurma()
aula_list = ListaAulas()
atividade_list = ListaAtividade()

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
            if verificar_vazio(alunos_list):
                print("\nNão há alunos Cadastrados no Sistema!!\n")
            else:
                print("\n----------Alunos Cadastrados no Sistema----------\n")
                alunos_list.print_list()
        elif op1 == '3':
            if verificar_vazio(alunos_list):
                print("\nNão há alunos Cadastrados no Sistema!!\n")
            else:
                buscar = str(input('\nDigite o RA do aluno que deseja buscar: ')).strip()
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
            if verificar_vazio(turma_list):
                print("\nNão há Turmas Cadastradas no Sistemas!!\n")
            else:
                print("\n---------Turmas Cadastradas no Sistema------------\n")
                turma_list.print_list()
        elif op1 == '3':
            if verificar_vazio(turma_list):
                print("\nNão há Turmas Cadastradas no Sistema!!\n")
            else:
                buscar = str(input("\nDigite o nome da Turma: ")).strip()
                print("\n----------ALUNOS NA TURMA {}----------\n".format(buscar))
                for aluno in alunos_list.list_():
                    if aluno.turma == buscar:
                        print(f"\n-{aluno.nome}\n")
                    else:
                        print("\nTURMA NÃO ENCONTRADA NO SISTEMA!!\n")
    elif op == '3':
        if verificar_vazio(turma_list):
            print("\nNão há Turmas Cadastradas no Sistema!!\n")
            print("Cadastre uma Turma para Registrar uma Aula!!\n")
        else:
            menu_aulas()
            if (op1 := str(input("\nDigite uma das opções acima: ")).strip()) == '1':
                aula_nova = registro_aula()
                verificar_aula = False
                for turma in turma_list.list_():
                    if turma.nome == aula_nova.turma:
                        aula_list.append(aula_nova)
                        print("\nAula cadastrada com sucesso✅!!\n")
                        verificar_aula = True
                if not verificar_aula:
                    print("\nA turma {} Não Existe Cadastrada no Sistema!!\n".format(aula_nova.turma))
            elif op1 == '2':
                buscar = str(input("\nDigite o nome da turma para saber suas aulas: ")).strip()
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
                print("\n------------Aulas da Turma {}--------------".format(buscar))
                for aulas in aula_list.list_():
                    if buscar == aulas.data:
                        print(f"\nData da Aula : {aulas.data} | Tema da Aula : {aulas.tema}\n")
                        verificar = True
                if not verificar:
                    print("\nTurma não Encontrada no Sistema!!\n")
    elif op == '4':
        if verificar_vazio(turma_list):
            print("\nNão há Turmas Cadastradas no Sistema!!\n")
            print("Cadastre uma Turma para Registrar uma Atividade!!\n")
        else:
            menu_atividade()
            if (op1 := str(input("\nDigite uma das opções acima: ")).strip()) == '1':
                print("\n------------Cadastro de Atividade------------")
                atividade_nova = cadastro_atividade()
                verificar_atividade = False
                for turma in turma_list.list_():
                    if turma.nome == atividade_nova.turma:
                        atividade_list.append(atividade_nova)
                        print("\nAtividade Cadastrada com Sucesso✅!!\n")
                        verificar_atividade = True
                if not verificar_atividade:
                    print("\nEstá Turma não Existe!!\n")
            elif op1 == '2':
                print("--------------Atividades Cadastradas no Sistema---------------")
                atividade_list.print_list()
            elif op1 == '3':
                print("\n---------------Busca Atividade--------------\n")
                buscar = str(input("\nDigite a turma que deseja ver as Atividades: ")).strip()
                verificar_atividade = False
                print("\n------------Atividades da Turma {}------------\n".format(buscar))
                for atividade in atividade_list.list_():
                    if atividade.turma == buscar:
                        print(f"\nNome da Atividade : {atividade.nome} | Data da Atividade : {atividade.data}")
                        verificar_atividade = True
                if not verificar_atividade:
                    print("\nNão há atividades na Turma {}\n".format(buscar))
    elif op == '5':
        print("-------------Bem Vindo a IA ACADEMY!!------------")
    elif op == '7':
        print("\nPROGRAMA ENCERRADO\n")
        break

    if continuar():
        print("\nPROGRAMA ENCERRADO\n")
        break
