from funcoes import turma_list ,alunos_list ,verificar_vazio , aula_list , atividade_list
from turma import Turma
from aluno import Aluno
from aula import Aula
from atividade import Atividade

def salvar_dados():
    with open("dados.txt", "w" , encoding="utf-8") as f:
        f.write("=== TURMAS ===\n")
        for turma in turma_list.to_list():
            f.write(f"{turma.nome};{turma.semestre};{turma.curso}\n")
        
        f.write("\n=== ALUNOS ===\n")
        for aluno in alunos_list.to_list():
            f.write(f"{aluno.nome};{aluno.turma}\n")
        
        f.write("\n=== AULAS ===\n")
        for aula in aula_list.to_list():
            f.write(f"{aula.data};{aula.turma};{aula.tema}\n")
        
        f.write("\n=== ATIVIDADES ===\n")
        for atividade in atividade_list.to_list():
            f.write(f"{atividade.nome};{atividade.data};{atividade.turma}\n")

    print("\nDados salvos com sucesso no sistema\n")

def carregar_dados():
        with open("dados.txt" , "r" , encoding="utf-8") as f:
            linhas = f.readlines()
        
        secao = None
        for linha in linhas:
            linha = linha.strip()
            if not linha:
                continue

            if linha.startswith("==="):
                if "TURMAS" in linha: secao = "turmas"
                elif "ALUNOS" in linha: secao = "alunos"
                elif "AULAS" in linha: secao = "aulas"
                elif "ATIVIDADES" in linha: secao = "atividades"
                continue

            partes = linha.split(";")

            if secao == "turmas":
                nome , semestre , curso= partes
                turma_list.append(Turma(nome,semestre,curso))
            elif secao == "alunos":
                nome,turma, = partes
                alunos_list.append(Aluno(nome,turma))
            elif secao == "aulas":
                data , turma , tema = partes
                aula_list.append(Aula(data,turma,tema))
            elif secao == "atividades":
                nome , turma , data = partes
                atividade_list.append(Atividade(nome,turma,data))


def consultar_turmas():
    if verificar_vazio(turma_list,"turma"):
        return
    print("\n--------------Registro Geral Turmas--------------\n")
    turma_list.print_list()


def aluno_por_turma():
    if verificar_vazio(alunos_list,"aluno"):
        return
    print("\n--------------Registro de Alunos por Turma--------------\n")
    alunos_list.print_list()


def aulas_por_turma():
    if verificar_vazio(turma_list,"turma"):
        return
    if verificar_vazio(aula_list,"aula"):
        return
    print("\n--------------Registro de Aulas por Turma--------------\n")
    aula_list.print_list()


def atividade_por_turma():
    if verificar_vazio(turma_list,"turma"):
        return
    if verificar_vazio(atividade_list,"atividade"):
        return
    print("\n--------------Registro de Atividades--------------\n")
    atividade_list.print_list()
