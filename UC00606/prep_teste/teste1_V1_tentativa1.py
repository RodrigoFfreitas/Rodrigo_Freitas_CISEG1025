
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# hora de começo: 16:10 
# hora da pausa: 17:20       fim da pausa: 18:58
# hora do fim:  19:10
# total de tempo gasto a fazer o teste: 82 minutos (tempo aproximado, pode ser menos ou mais pq pequenas interupções a meio)
# total de consultas feitas (2) 1- Ver como funcionava o listar tudo  2- Ver como funciona o Ordenar
#
# notas: o ordenar não funciona, estudar mais a fundo! |--| 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



listaNomeLivros = []
listaAutor = []
listaAnoPublicacao = []
userInputProcuraLivros = ""


def printListaLivros():
    for i in range(len(listaNomeLivros)):
        print(f"Indice: {i} | Nome: {listaNomeLivros[i]} | Autor: {listaAutor[i]} | Ano de Publicação: {listaAnoPublicacao[i]}")

def cadastrarLivros():
    print("Insira o titulo do Livro que deseja inserir.")
    listaNomeLivros.append(input())
    
    print("Insira o nome do Autor do Livro.")
    listaAutor.append(input())
    
    print("Insira o ano em que Livro foi publicado.")
    listaAnoPublicacao.append(input())

def procurarLivros():
    
    # Pede ao user se quer pesquisar pelo titulo ou pelo autor
    userInputProcuraLivros = input('Deseja procurar o livro pelo titulo ou pelo autor?\n')
    
    # se a resposta for titulo ou titulos
    if userInputProcuraLivros == "titulo" or userInputProcuraLivros == "titulos":
        
        nomeTituloProcura = input('Insira o Titulo do livro ao qual deseja encontrar: ')
        
        for i in range(len(listaNomeLivros)):
            if listaNomeLivros[i] == nomeTituloProcura:
                print(f"Indice: {i} | Nome: {listaNomeLivros[i]} | Autor: {listaAutor[i]} | Ano de Publicação: {listaAnoPublicacao[i]}")
            else:
                continue
        
    elif userInputProcuraLivros == "autor" or userInputProcuraLivros == "autores":
        print("segunda fase do if")
        
        nomeAutorProcura = input('Insira o Autor do livro ao qual deseja encontrar: ')
        
        for i in range(len(listaAutor)):
            if listaAutor[i] == nomeAutorProcura:
                print(f"Indice: {i} | Nome: {listaNomeLivros[i]} | Autor: {listaAutor[i]} | Ano de Publicação: {listaAnoPublicacao[i]}")
            else:
                continue
        
        
    else:
        print("Deve escrever no ecrã autor ou titulo! (certifique-se de que usou apenas minusculas)")
    
def excluirLivros():
    print("Certifique-se que sabe o numero do Indice do Livro ao qual deseja Apagar")
    
    confimacaoExcluirLivro=input('Deseja Continuar? (s/n): ')
    
    if confimacaoExcluirLivro == "s" or confimacaoExcluirLivro == "sim":
            indexLivroExcluir = int(input('Insira o Indice do Livro a Excluir: '))
            listaNomeLivros.pop(indexLivroExcluir)

def ordenarLivros():
    userInputOrdenarLivros = input('Deseja ordenar por titulo ou pelo autor?\n')
    
    
    if userInputOrdenarLivros == "titulo" or userInputOrdenarLivros == "titulos":
        
        listaNomeLivros.sort()
        for i in range(len(listaNomeLivros)):
            print(f"Indice: {i} | Nome: {listaNomeLivros[i]} | Autor: {listaAutor[i]} | Ano de Publicação: {listaAnoPublicacao[i]}")

        
        
    elif userInputOrdenarLivros == "autor" or userInputOrdenarLivros == "autores":
        
        listaAutor.sort()
        for i in range(len(listaAutor)):
            print(f"Indice: {i} | Autor: {listaAutor[i]} | Nome: {listaNomeLivros[i]} | Ano de Publicação: {listaAnoPublicacao[i]}")
        
        
    else:
        print("Deve escrever no ecrã autor ou titulo! (certifique-se de que usou apenas minusculas)")


while True:
    
    print("1 - Cadastrar Livros")
    print("2 - Procurar por Livros")
    print("3 - Excluir Livros")
    print("4 - Ordenar Livros")
    print("5 - Listar todos os Livros cadastrados")
    print("6 - Sair do Programa")


    userInput=input("Escolha uma das seguintes opções: ") 
    
    match userInput:
        
        case "1":
            cadastrarLivros()
      
        case "2":
            procurarLivros()
            
        case "3":
            excluirLivros()
            
        case "4":
            ordenarLivros()
            
        case "5":
            print("A listar todos os Livros cadastrados: ")
            printListaLivros() 
       
        case "6":
            print("A Sair do programa")
            break
        
        case _:
            print("Insira um numero de 1 a 6!")
