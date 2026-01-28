listaMarcas = []
listaModelos = []


while True:
    
    
    print("1 - Cadastrar Marcas e Modelos")
    print("2 - Procurar por Marcas ou Modelos")
    print("3 - Excluir Marcas ou Modelos")
    print("4 - Sair do Programa")
    userInput=input("Escolha uma das seguintes opções: ")

    
    
    
    match userInput:
        case "1":
            print("1 - Cadastrar Marcas")
            print("2 - Cadastrar Modelos")
            print("3 - Voltar ao Menu Inicial")
            userInputCadastro=input("Escolha uma das seguintes opções: ")
        case "2":
            print("1 - Procurar Marcas")
            print("2 - Procurar Modelos")
            print("3 - Voltar ao Menu Inicial")
            userInputProcurar=input("Escolha uma das seguintes opções: ")
            
        case "3":
            print("1 - Procurar Marcas")
            print("2 - Procurar Modelos")
            print("3 - Voltar ao Menu Inicial")
            userInputExcuir=input("Escolha uma das seguintes opções: ")
            
            
            
            
        case "4":
            print("A sair")
            break