from aluno import Aluno
from turma import Turma
from atividade import Atividade
from aula import Aula
from lista_alunos import ListaAlunos
from lista_turma import ListaTurma
from lista_aula import ListaAulas
from lista_atividade import ListaAtividade

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

def menu_princiapal_ia():
    if verificar_vazio(alunos_list):
        print("\nNão há alunos cadastrados no sistema!!\n")
        print("Cadastre aluno para poder usar a IA ACADEMY\n")
    else:
        menu_ia()
        if (op1 := str(input("Digite umas das opções acima:")).strip()) == '1':
            sugerir_atividade()
        elif op1 == '2':
            sugerir_foco()


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



def sugerir_atividade():
    print("\n------------Sugestão IA--------------\n")
    if verificar_vazio(alunos_list):
        print("Não há alunos cadastrados no Sistema\n")
        return

    elif verificar_vazio(atividade_list):
        print("\nNão há atividades cadastradas\n!!")
        return

    else:

        turma_alvo = str(input("Digite o nome da turma: "))
        turma_existe = any(aluno.turma == turma_alvo for aluno in alunos_list.list_())

        if not turma_existe:
            print("\nEsta turma não existe!!\n")
            return 

        atividades = [ativ for ativ in atividade_list.list_() if ativ.turma == turma_alvo]
        ultima_atividade = atividades[-1]

    if 'revisão' in ultima_atividade.nome:
        print("\nA revisão ja foi realizada. Sugiro que faça uma Avaliação para solidificar o conhecimento!\n")
    elif 'trabalho' in ultima_atividade.nome or 'projeto' in ultima_atividade.nome:
        print("\nO projeto já foi concluido. Sugiro que faça a apresentação\n")
    elif 'avaliação' in ultima_atividade.nome or 'prova' in ultima_atividade.nome:
        print("\nA avaliação foi concluida. Sugiro que faça uma discussão para possiveis erros\n")
    else:
        print("\nSugiro uma revisão geral\n")
    
    print("-"*20)
    

def sugerir_foco():
    if verificar_vazio(alunos_list):
        print("\nNão há aluno cadastrados no Sistema!!\n")
        return
    print("\n----------Análise de Foco (IA Simples)----------\n")
    num_alunos = {}

    for aluno in alunos_list.list_():
        turma = aluno.turma
        num_alunos[turma] = num_alunos.get(turma, 0) + 1
    
    if not num_alunos:
        print("\nNenhuma turma com alunos cadastrados!!\n")
        return
    
    turma_ordenada = sorted(num_alunos.items()  , key = lambda item : item[1] , reverse = True)

    turma_maior = turma_ordenada[0]
    nome_turma = turma_maior[0]
    qtd_alunos = turma_maior[1]

    print(f"\nAnálise : A turma com mais aluno é '{nome_turma}' com {qtd_alunos} alunos\n")
    print(f"Foco da IA : Por ter mais alunos esta turma exige maior atenção e possivelmente mais atividade\n")

    if len(turma_ordenada) > 1:
        turma_menor = turma_ordenada[-1]
        print(f"Obeservação: A turma '{turma_menor[0]}' tem poucos alunos ({turma_menor[1]}). Considere um feedback mais aprofundado para eles.\n")

    
    
alunos_list = ListaAlunos()
turma_list  = ListaTurma()
aula_list   = ListaAulas()
atividade_list = ListaAtividade()
