from operacao_alunos import *
from operacao_atividade import *
from operacao_aula import *
from operacao_ia import *
from operacao_turma import *
from operacao_relatorio import *


def menu_principal():
    print("\n\n------------Bem Vindo ao Menu Principal------------")
    print("\n1-Gerenciar Alunos")
    print("2-Gerenciar Turmas")
    print("3-Gerenciar Aulas")
    print("4-Gerenciar Atividades")
    print("5-Inteligencia Artificial")
    print("6-Relatorios e Consultas")
    print("7-sair")


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
    print("\n-------------🤖Bem Vindo a IA ACADEMY!!------------\n")
    print("1-Sugerir Atividade")
    print("2-Foco Turma")
    print("3-Chatbot")


def menu_relatorio_e_consulta():
    print("\n--------------Relatorios e Consulta--------------\n")
    print("1-Registro Geral\n")
    print("2-Relatorio de Alunos por Turma\n")
    print("3-Relatorio de Aulas por Turma\n")
    print("4-Relatorio de Atividades por Turma\n")


def encerrar():
    print("Programa Encerrardo")
    

def menu_aula_principal():
    if verificar_vazio(turma_list,"turma"):
        return
    menu_aulas()
    opcao = ler_texto()

    opcoes = {
        '1' : registrar_aula_opcao,
        '2' : listar_aula_turma_opcao,
        '3' : consulta_aula_data_opcao,
        '4' : excluir_aula_opcao  
    }

    funcao = opcoes.get(opcao)
    if funcao:
        funcao()
    else:
        print("\nERRO!!Valor Inválido!!\n")


def menu_principal_turma():
    menu_turma()
    opcao = ler_texto()

    opcoes = {
        '1' : cadastrar_turma_opcao,
        '2' : listar_turmas_opcao,
        '3' : buscar_turma_opcao,
        '4' : excluir_turma_opcao
    }

    funcao = opcoes.get(opcao)
    if funcao:
        funcao()
    else:
        print("Digite um valor válido!!")


def menu_principal_aluno():
    menu_aluno()
    opcao = ler_texto()

    opcoes = {
        '1' : cadastrar_aluno_opcao,
        '2' : listar_alunos_opcao,
        '3' : buscar_aluno_opcao,
        '4' : excluir_aluno_opcao
    }

    funcao = opcoes.get(opcao)
    if funcao:
        funcao()
    else:
        print("\nERRO! VALOR INVÁLIDO!!\n")


def menu_principal_atividade():

        menu_atividade()
        opcao = ler_texto()

        opcoes = {
            '1' : cadastrar_atividade_opcao,
            '2' :  listar_atividades_opcao,
            '3' : buscar_atividade_opcao,
            '4' : excluir_atividade_opcao
        }
        funcao = opcoes.get(opcao)
        if funcao:
            funcao()
        else:
            print("\nERRO!VALOR INVÁLIDO!!\n")


def menu_princiapal_ia():
    if verificar_vazio(alunos_list,"aluno"):
        return

    menu_ia()
    opcao = ler_texto()

    opcoes = {
        '1' : sugerir_atividade,
        '2' : sugerir_foco,
        '3' : iniciar_chatbot
    }
    funcao = opcoes.get(opcao)
    if funcao:
        funcao()
    else:
        print("\nDigite um valor valido!\n")


def menu_principal_relatorio():
    menu_relatorio_e_consulta()
    opcao = ler_texto()

    opcoes = {
        '1' : consultar_turmas,
        '2' : aluno_por_turma,
        '3' : aulas_por_turma,
        '4' : atividade_por_turma,
    }
    funcao = opcoes.get(opcao)
    if funcao:
        funcao()
    else:
        print("\nValor invalido\n")
