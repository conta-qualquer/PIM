from funcoes import ler_texto , limpar_tela , continuar
from menus import * 


def sistema_academico():

    carregar_dados()
    

    while True:
        limpar_tela()
        menu_principal()

        opcoes = {
            '1' : menu_principal_aluno,
            '2' : menu_principal_turma,
            '3' : menu_aula_principal,
            '4' : menu_principal_atividade,
            '5' : menu_princiapal_ia,
            '6' : menu_principal_relatorio,
            '7' : encerrar
        }

        opcao = ler_texto()
        funcao = opcoes.get(opcao)
        if funcao:
            funcao()
            if opcao == '7':
                salvar_dados()
                break
            if continuar():
                print("\nPROGRAMA ENCERRADO\n")
                salvar_dados()
                break
        else:
            print("\nDigite um valor válido\n")

if __name__ == "__main__":
    sistema_academico()
