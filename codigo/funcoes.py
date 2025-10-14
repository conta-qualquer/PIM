from aluno import Aluno
from turma import Turma
from atividade import Atividade
from aula import Aula
from lista_alunos import ListaAlunos
from lista_turmas import ListaTurma
from lista_aulas import ListaAulas
from lista_atividades import ListaAtividade

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
    print("4-Excluir Aluno")

def menu_turma():
    print("\n----------GERENCIAR TURMA----------")
    print("\n1-Cadastrar Turma")
    print("2-Listar Turmas")
    print("3-Ver alunos da Turma")
    print("4-Excluir Turma")

def menu_aulas():
    print("\n----------GERENCIAR AULAS----------")
    print("\n1-Registrar Aulas")
    print("2-Listar Aulas de uma Turma")
    print("3-Consulta aulas por Data")
    print("4-Excluir Aula")

def menu_atividade():
    print("\n----------GERENCIAR ATIVIDADE----------")
    print("\n1-Cadastrar Atividade")    
    print("2-Listar Atividade")    
    print("3-Consulta Atividade por Turma")
    print("4-Excluir Atividade")

def menu_ia():
    print("\n-------------Bem Vindo a IA ACADEMY!!------------\n")
    print("1-Sugerir Atividade")
    print("2-Foco Turma\n")


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

def continuar():
        op = str(input("Deseja voltar para o menu principal ? :  [S/N]")).lower().strip()
        if op == 'n':
             return op == 'n'

def verificar_vazio(lista):
        return True if len(lista) == 0 else False

def menu_principal_aluno():
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
            verificar_aluno = False
            for aluno in alunos_list.list_():
                if buscar == aluno.id:
                    print('\n------------ALUNO ENCONTRADO COM SUCESSO--------------\n')
                    print('{}\n'.format(aluno))
                    verificar_aluno = True
            if not verificar_aluno:
                print("\nO aluno {} não foi encontrado no sistema\n".format(buscar))
    elif op1 == '4':
        if verificar_vazio(alunos_list):
            print("\nNão há alunos cadastrados\n")
        else:
            buscar = str(input("\nDigite o nome do aluno que deseja excluir : ")).strip()
            verificar_aluno = False
            for aluno in alunos_list.list_():
                if aluno.nome == buscar:
                    alunos_list.remove(aluno)
                    print("\nAluno {} excluido com sucesso ✅!!\n".format(buscar))
                    verificar_aluno = True
            if not verificar_aluno:
                print("\nO aluno {} não está cadastrado no sistema\n".format(buscar))
    else:
        print("\nERRO! VALOR INVÁLIDO!!\n")

def menu_principal_turma():
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
            verificar_turma = False
            print("\n----------ALUNOS NA TURMA {}----------\n".format(buscar))
            for aluno in alunos_list.list_():
                if aluno.turma == buscar:
                    print(f"\n-{aluno.nome}\n")
                    verificar_turma = True
            if not verificar_turma:
                print("\nTURMA NÃO ENCONTRADA NO SISTEMA!!\n")
    elif op1 == '4':
        if verificar_vazio(turma_list):
            print("\nNão há turmas cadastradas no sistema\n")
        else:
            buscar = str(input("\nDigite o nome da turma que deseja excluir: ")).strip()
            verificar_turma = False
            for turma in turma_list.list_():
                if turma.nome == buscar:
                    turma_list.remove(turma)
                    print("\nTurma {} excluida com sucesso!!\n")
                    verificar_turma = True
            if not verificar_turma:
                print("\nTurma não encontrada no sistema!\n")
    else:
        print("\nERRO!! VALOR INVÁLIDO!!\n")


def menu_aula_principal():
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
                print(f"\nData da Aula : {aulas.data} | Tema da Aula : {aulas.tema}\n")
                verificar = True
        if not verificar:
            print("\nAula não Encontrada!!\n")
    elif op1 == '3':
        buscar = str(input("\nDigite a data da aula para consulta-lá: ")).strip()
        verificar = False
        print("\n------------Aulas da Data {}--------------".format(buscar))
        for aulas in aula_list.list_():
            if buscar == aulas.data:
                print(f"\nData da Aula : {aulas.data} | Tema da Aula : {aulas.tema} | Turma : {aulas.turma}\n")
                verificar = True
        if not verificar:
            print("\nData não Encontrada!!\n")
    elif op1 == '4':
        if verificar_vazio(aula_list):
            print("\nNão há aulas cadastradas no sistema!!\n")
        else:
            buscar_data = str(input("\nDigite data da aula a ser excluida: ")).strip()
            buscar_tema = str(input("\nDigite o tema da aula a ser excluida: ")).strip()
            verificar_aula = False
            for aula in aula_list.list_():
                if aula.data == buscar_data and aula.tema == buscar_tema:
                    aula_list.remove(aula)
                    verificar_aula = True
                    print("\nAula excluida com sucesso!!\n")
            if not verificar_aula:
                print("\nAula não Encontrada no Sistema!!\n")
    else:
        print("\nERRO!!Valor Inválido!!\n")

def menu_principal_atividade():
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
            print("\n--------------Atividades Cadastradas no Sistema---------------\n")
            if verificar_vazio(atividade_list):
                print("\nNão há atividades cadastradas no Sistema\n")
            atividade_list.print_list()
        elif op1 == '3':
            print("\n---------------Busca Atividade--------------\n")
            buscar = str(input("\nDigite a turma que deseja ver as Atividades: ")).strip()
            verificar_atividade = False
            print("\n------------Atividades da Turma {}------------\n".format(buscar))
            for atividade in atividade_list.list_():
                if atividade.turma == buscar:
                    print(f"\nNome da Atividade : {atividade.nome} | Data da Atividade : {atividade.data}\n")
                    verificar_atividade = True
            if not verificar_atividade:
                print("\nNão há atividades na Turma {}\n".format(buscar))
        elif op1 == '4':
            if verificar_vazio(atividade_list):
                print("\nNão existe atividade cadastrada no sistema!\n")
            else:
                buscar_atividade = str(input("\nDigite o nome da atividade que deseja excluir: ")).strip()
                verificar_atividade = False
                for atividade in atividade_list.list_():
                    if atividade.nome == buscar_atividade:
                        atividade_list.remove(atividade)
                        verificar_atividade = True
                        print("\nAtividade excluida com sucesso!!\n")
                if not verificar_atividade:
                    print("\nAtividade Não Encontrada no Sistema!!\n")
        else:
            print("\nERRO!VALOR INVÁLIDO!!\n")

def sugerir_atividade(turmas , atividades):
    print("\n------------Sugestão de Atividade (IA Simples)--------------")
    if verificar_vazio(turmas):
        print("\nNão há turmas cadastradas no sistema!!\n")
        return
    
    turma_alvo = str(input("De qual turma você gostaria de receber sugestções de atividade: ")).strip()
    turma_existe = any(turma.nome == turma_alvo for turma in turma_list.list_())

    if not turma_existe:
        print(f"A turma '{turma_alvo}' não está encontrada")
        return
    
    pass
alunos_list = ListaAlunos()
turma_list = ListaTurma()
aula_list = ListaAulas()
atividade_list = ListaAtividade()
