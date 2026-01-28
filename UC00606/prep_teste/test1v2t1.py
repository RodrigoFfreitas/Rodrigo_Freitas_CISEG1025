
numAlunos = 0
listaNomeAluno = []
listaTurmaAluno = []
perguntaDesejaContinuar = ''


while numAlunos <= 100:
    
    print("1 - Registar novo aluno")
    print("2 - Pesquisar alunos por nome ou turma")
    print("3 - Eliminar aluno por posição")
    print("4 - Ordenar por aluno de A-Z")
    print("5 - Listar Alunos e turmas que cada aluno pertence")
    print("6 - Sair do programa")
    
    userInputMenu=int(input("Escolha uma das opções anteriores: "))
    
    match userInputMenu:
        case 1:
            print('-- Resistro de alunos --')
            print("Insira o nome do aluno")
            listaNomeAluno.append(input())
            
            print("Insira a Turma do respetivo aluno")
            listaTurmaAluno.append(input()) 
            
            numAlunos+=1
            
        case 2:
            print("2")

            userInputProcuraAlunos = input('Deseja procurar o aluno pelo Nome ou pela turma?\n')
            
            if userInputProcuraAlunos == "Aluno" or userInputProcuraAlunos == "aluno":
                
                nomeAlunoProcura = input('Insira o nome do aluno que deseja encontrar: ')
                
                for i in range(len(listaNomeAluno)):
                    if listaNomeAluno[i] == nomeAlunoProcura:
                       print(f"Indice: {i} | Nome: {listaNomeAluno[i]} | Turma: {listaTurmaAluno[i]}")
                    else:
                        continue
                
            elif userInputProcuraAlunos == "Turma" or userInputProcuraAlunos == "turma":
                
                nomeTurmaProcura = input('Insira a Turma do aluno que deseja encontrar: ')
                
                for i in range(len(listaTurmaAluno)):
                    if listaTurmaAluno[i] == nomeTurmaProcura:
                        print(f"Indice: {i} | Nome: {listaNomeAluno[i]} | Turma: {listaTurmaAluno[i]}")
                    else:
                        continue
            
        case 3:
            print("Confirme se sabe qual o indice do aluno que deseja excluir!")
            
            perguntaDesejaContinuar=input('Deseja Continuar? (s/n): ')
            
            if perguntaDesejaContinuar == "s" or perguntaDesejaContinuar == "sim":
                indexAlunoExcluir = int(input('Insira o Indice do Aluno a Excluir: '))
                listaNomeAluno.pop(indexAlunoExcluir)
                listaTurmaAluno.pop(indexAlunoExcluir)
            else:
                continue
            
        case 4:
            print("4")
            
            listaNomeAluno.sort()
            for i in range(len(listaNomeAluno)):
                print(f"Indice: {i} | Nome: {listaNomeAluno[i]} | Turma: {listaTurmaAluno[i]}")
            
        case 5:
            print("-- Listagem de alunos --")
            
            for i in range(len(listaNomeAluno)):
                print(f"Indice: {i} | Nome: {listaNomeAluno[i]} | Turma: {listaTurmaAluno[i]}")
                
            perguntaDesejaContinuar=input('Deseja Continuar? (s/n): ')
            
            if perguntaDesejaContinuar == "s" or perguntaDesejaContinuar == "sim":
                continue
                  
        case 6:
            print("A sair do Programa!")
            break
        case _:
            print("Escolha inválida deve escolher um numero de 1 a 6!")