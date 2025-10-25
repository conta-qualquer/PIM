from funcoes import *
from cadastros import registro_aula


def registrar_aula_opcao():
    aula_nova = registro_aula()
    for turma in turma_list.to_list():
        if turma.nome == aula_nova.turma:
            aula_list.append(aula_nova)
            print("\nAula cadastrada com sucesso✅!!\n")
            return
    print(f"\nA turma {aula_nova.turma} Não Existe Cadastrada no Sistema!!\n")


def listar_aula_turma_opcao():
    buscar_aula = str(input("\nDigite o nome da turma para saber suas aulas: ")).strip()
    print(f"\n----------Aulas da Turma {buscar_aula}----------")
    for aulas in aula_list.to_list():
        if aulas.turma == buscar_aula:
            print(f"\nData da Aula : {aulas.data} | Tema da Aula : {aulas.tema}\n")
            return
    print("\nAula não Encontrada!!\n")


def consulta_aula_data_opcao():
    buscar_aula = str(input("\nDigite a data da aula para consulta-lá: ")).strip()
    print(f"\n------------Aulas da Data {buscar_aula}--------------")
    for aulas in aula_list.to_list():
        if buscar_aula == aulas.data:
            print(f"\nData da Aula : {aulas.data} | Tema da Aula : {aulas.tema} | Turma : {aulas.turma}\n")
            return
    print("\nData não Encontrada!!\n")


def excluir_aula_opcao():
    if verificar_vazio(aula_list,"turma"):
        return
    buscar_data = str(input("\nDigite data da aula a ser excluida: ")).strip()
    buscar_tema = str(input("\nDigite o tema da aula a ser excluida: ")).strip()
    for aula in aula_list.to_list():
        if aula.data == buscar_data and aula.tema == buscar_tema:
            aula_list.remove(aula)
            print("\nAula excluida com sucesso!!\n")
            return
    print("\nAula não Encontrada no Sistema!!\n")
