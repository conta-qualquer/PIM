from funcoes import verificar_vazio , alunos_list , atividade_list , turma_list

def sugerir_atividade():
    print("\n------------🤖Sugestão IA--------------\n")
    if verificar_vazio(alunos_list,"aluno"):
        return

    if  verificar_vazio(atividade_list,"atividade"):
        print("\nNão há atividades cadastradas!!\n")
        return

    turma_alvo = str(input("Digite o nome da turma: "))

    found = False
    for atividade in atividade_list.to_list():
        if atividade.turma == turma_alvo:
            found = True
            continue
    if not found:
        print("\nNão há atividades cadastradas nesta turma!\n")
        return
    
    turma_existe = any(aluno.turma == turma_alvo for aluno in alunos_list.to_list())

    if not turma_existe:
        print("\nEsta turma não há alunos !!\n")
        return 

    atividades = [ativ for ativ in atividade_list.to_list() if ativ.turma == turma_alvo]
    ultima_atividade = atividades[-1]

    if 'revisão' in str(ultima_atividade.nome).lower():
        print("\nA revisão ja foi realizada. Sugiro que faça uma Avaliação para solidificar o conhecimento!\n")
    elif 'trabalho' in str(ultima_atividade.nome).lower() or 'projeto' in str(ultima_atividade.nome).lower():
        print("\nO projeto já foi concluido. Sugiro que faça a apresentação\n")
    elif 'avaliação' in str(ultima_atividade.nome).lower() or 'prova' in str(ultima_atividade.nome).lower():
        print("\nA avaliação foi concluida. Sugiro que faça uma discussão para possiveis erros\n")
    else:
        print("\nSugiro uma revisão geral\n")
    
    print("-"*50)
    
def chatbot(pergunta):
    arvore_chatbot = {
        "atividade":{
            "resposta" : "Você pode consultar suas atividade cadastradas no menu 'Atividade'"
        },

        "aula" : {
            "resposta" : "As aulas estão disponiveis com data e tema no menu 'Aula'"
        },

        "aluno" : {
            "resposta" : "Os aluno estão listados junto à turma e RA no menu 'ALUNOS'"
        },

        "turma" : {
            "resposta" : "As turmas podem ser visualizadas no menu 'Turmas' , com curso e semestre" 
        }
    }

    pergunta = pergunta.lower()
    for chave,resposta in arvore_chatbot.items():
        if chave in pergunta:
            return f"{resposta}"
    return f"\nDesculpe, não entendi sua dúvida. Tente perguntar sobre 'atividade','aula','aluno' ou 'turma'.\n"

def iniciar_chatbot():
    print("\n🤖 Chatbot acadêmico - digite 'sair' para encerrar")
    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() in ["sair","exit"]:
            print("\nChatbot: Até logo!\n")
            break
        resposta = chatbot(pergunta)
        print(f"\nChatbot: {''.join(resposta)}")

def sugerir_foco():
    if verificar_vazio(turma_list,"turma"):
        return

    contagem_turma = {}
    for aluno in alunos_list.to_list():
        turma = aluno.turma
        contagem_turma[turma] = contagem_turma.get(turma , 0) + 1
    
    if not contagem_turma:
        print("\nNão há aluno cadastrados na turma\n")
    
    turma_ordenada = sorted(contagem_turma.items() , key = lambda item : item[1] , reverse = True)
    maior_turma = turma_ordenada[0]
    nome_turma = maior_turma[0]
    qtd_turma = maior_turma[1]
    print(f"\n--------------🤖Foco na Turma {nome_turma}--------------")
    print(f"\n🤖Sugestão IA : A maior turma é a {nome_turma} com {qtd_turma} alunos , foco principal em atividades e atividades extras!!\n")
