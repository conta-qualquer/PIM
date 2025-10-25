from cadastros import cadastro_turma
from funcoes import turma_list , verificar_vazio , alunos_list

def cadastrar_turma_opcao():
    turma_nova = cadastro_turma()
    for turma in turma_list.to_list():
        if turma.nome == turma_nova.nome:
            print("\nNão pode haver Turmas com nomes iguais\1!!\n")
            return
    turma_list.append(turma_nova)
    print("\nTurma Cadastrada com Sucesso ✅!!\n")


def listar_turmas_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    print("\n---------Turmas Cadastradas no Sistema------------\n")
    turma_list.print_list()


def buscar_turma_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    buscar_turma = str(input("\nDigite o nome da Turma: ")).strip()
    found = False
    print(f"\n----------ALUNOS NA TURMA {buscar_turma}----------\n")
    for aluno in alunos_list.to_list():
        if aluno.turma == buscar_turma:
            print(f"-{aluno.nome}\n")
            found = True
    if not found:
        print("Não há alunos cadastrados no sistema\n")


def excluir_turma_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    buscar_turma = str(input("\nDigite o nome da turma que deseja excluir: ")).strip()
    for turma in turma_list.to_list():
        if turma.nome == buscar_turma:
            turma_list.remove(turma)
            print(f"\nTurma {buscar_turma} excluida com sucesso!!\n")
            return
    print("\nTurma não encontrada no sistema!\n")
