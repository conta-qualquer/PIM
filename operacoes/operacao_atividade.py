from funcoes import verificar_vazio , turma_list , atividade_list
from cadastros import cadastro_atividade


def cadastrar_atividade_opcao():
    if verificar_vazio(turma_list,"turma"):
        return
    print("\n------------Cadastro de Atividade------------")
    atividade_nova = cadastro_atividade()
    for turma in turma_list.to_list():
        if turma.nome == atividade_nova.turma:
            atividade_list.append(atividade_nova)
            print("\nAtividade Cadastrada com Sucesso✅!!\n")
            return
    print("\nEstá Turma não Existe!!\n")


def listar_atividades_opcao():
    print("\n--------------Atividades Cadastradas no Sistema---------------\n")
    if verificar_vazio(atividade_list,"atividade"):
        return
    atividade_list.print_list()


def buscar_atividade_opcao():
    print("\n---------------Busca Atividade--------------\n")
    buscar_atividade = str(input("\nDigite a turma que deseja ver as Atividades: ")).strip()
    verificar_atividade = False
    print(f"\n------------Atividades da Turma {buscar_atividade}------------\n")
    for atividade in atividade_list.to_list():
        if atividade.turma == buscar_atividade:
            print(f"\nNome da Atividade : {atividade.nome} | Data da Atividade : {atividade.data}\n")
            verificar_atividade = True
    if not verificar_atividade:
        print(f"\nNão há atividades na Turma {buscar_atividade}\n")


def excluir_atividade_opcao():
    if verificar_vazio(atividade_list,"atividade"):
        return    
    buscar_atividade = str(input("\nDigite o nome da atividade que deseja excluir: ")).strip()
    busca_turma = str(input("Digite o nome da turma que deseja excluir a atividade: ")).strip()
    for atividade in atividade_list.to_list():
        if atividade.nome == buscar_atividade and atividade.turma == busca_turma:
            atividade_list.remove(atividade)
            print("\nAtividade excluida com sucesso!!\n")
            return
    print("\nAtividade Não Encontrada no Sistema!!\n")
