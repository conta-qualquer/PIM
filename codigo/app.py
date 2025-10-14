from funcoes import *



while True:
    
    menu_principal()

    op = str(input("\nDigite uma das opção acima: "))

    if op == '1':

        menu_aluno()
        menu_principal_aluno()
            
    elif op == '2':

        menu_turma()
        menu_principal_turma()

    elif op == '3':

        menu_aulas()
        menu_aula_principal()

    elif op == '4':

        menu_atividade()
        menu_principal_atividade()
        
    elif op == '5':

        menu_ia()

    elif op == '6':

        pass

    elif op == '7':

        print("\nPROGRAMA ENCERRADO\n")
        break

    else:

        print("\nDigite um valor válido\n")


    if continuar():
        print("\nPROGRAMA ENCERRADO\n")
        break
