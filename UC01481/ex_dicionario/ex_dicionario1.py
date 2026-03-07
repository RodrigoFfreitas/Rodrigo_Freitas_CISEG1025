alunos = []

while True:
    print("\n--- Menu ---")
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    userMenuInput = input("Escolha uma opção: ")

    match userMenuInput:
        case "1":
            nome = input("Nome do aluno: ")
            idade = input("Idade do aluno: ")
            curso = input("Curso do aluno: ")

            aluno = {
                "nome": nome,
                "idade": idade,
                "curso": curso
            }

            alunos.append(aluno)
        case "2":
            if len(alunos) == 0:
                print("Não existem alunos cadastrados.")
            
            else:
                for aluno in alunos:
                    print("nome:", aluno["nome"])
                    print("idade:", aluno["idade"])
                    print("curso:", aluno["curso"])
                    print()
            
        case "3":
            break
        
        case _:
            print("Opção inválida.")            
