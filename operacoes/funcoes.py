from os import system
from lista_alunos import ListaAlunos
from lista_aula import ListaAulas
from lista_atividade import ListaAtividade
from lista_turma import ListaTurma

def limpar_tela():
    cmd = 'cls'
    return system(cmd)


def continuar():
    op = str(input("Deseja voltar para o menu principal ? :  [S/N]")).lower().strip()
    if op == 'n':
        return op == 'n'


def verificar_vazio(lista,tipo):
    if len(lista) == 0:
        print(f"\nLista de {tipo}s vazia\n")
        return True
    return False


def ler_texto():
    opcao = str(input("\nDigite umas das opçoes acima: ")).strip()
    return opcao

    
alunos_list = ListaAlunos()
turma_list  = ListaTurma()
aula_list   = ListaAulas()
atividade_list = ListaAtividade()
