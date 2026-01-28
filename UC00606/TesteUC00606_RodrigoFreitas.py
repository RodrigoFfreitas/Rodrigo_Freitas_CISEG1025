listaTituloFilme = []
listaDiretorFilme = []
listaAnoLancamentoFilme = []
listaGeneroFilme = []
nFilmesCadastrados = 0



def adicionarFilmes():
    global nFilmesCadastrados
    
    if nFilmesCadastrados <= 100:
        print('-- Adicionar Filmes --')
        print("Insira o titulo do filme")
        listaTituloFilme.append(input())
                        
        print("Insira o nome do diretor do filme")
        listaDiretorFilme.append(input()) 
                        
        print("Insira o ano de lançamento do filme")
        listaAnoLancamentoFilme.append(input())
                        
        print("Insira o genero do filme")
        listaGeneroFilme.append(input())
    else:
        print('Existem 100 Filmes cadastrados de momento, e por isso, não é possivel cadastrar mais filmes!')
            
    nFilmesCadastrados+=1
   
def procurarFilmes():
    userInputProcuraFilmes = input('Deseja procurar o filme por titulo, diretor ou genero?\n')
            
    if userInputProcuraFilmes == "Titulo" or userInputProcuraFilmes == "titulo":
                
        tituloFilmeProcura = input('Insira o titulo do filme que deseja encontrar: ')
                
        for i in range(len(listaTituloFilme)):
            if listaTituloFilme[i] == tituloFilmeProcura:
                print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")


                
                
    elif userInputProcuraFilmes == "Diretor" or userInputProcuraFilmes == "diretor":
                
        diretorFilmeProcura = input('Insira o diretor do filme que deseja encontrar: ')
                
        for i in range(len(listaDiretorFilme)):
            if listaDiretorFilme[i] == diretorFilmeProcura:
                print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")

                    
                    
    elif userInputProcuraFilmes == "Genero" or userInputProcuraFilmes == "genero":
                
        generoFilmeProcura = input('Insira o genero do filme que deseja encontrar: ')
                
        for i in range(len(listaGeneroFilme)):
            if listaGeneroFilme[i] == generoFilmeProcura:
                print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")
                
            
    else:
        print('A opção escolhida é inválida, a voltar ao menu inicial!')
            
def listarFilmes():
    for i in range(len(listaTituloFilme)):
                print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")

def ordenarFilmes():
    userInputOrdenarFilmes = input('Deseja Ordenar o filme por titulo, diretor ou Ano de lancamento?\n')
            
    if userInputOrdenarFilmes == "Titulo" or userInputOrdenarFilmes == "titulo":
                
        listaTituloFilme.sort()
        for i in range(len(listaTituloFilme)):
            print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")

                
    elif userInputOrdenarFilmes == "Diretor" or userInputOrdenarFilmes == "diretor":
                
        listaDiretorFilme.sort()
        for i in range(len(listaDiretorFilme)):
            print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")

                
    elif userInputOrdenarFilmes == "Ano de lancamento" or userInputOrdenarFilmes == "ano de lancamento":
                
        listaAnoLancamentoFilme.sort()
        for i in range(len(listaAnoLancamentoFilme)):
            print(f"Indice: {i} | Titulo: {listaTituloFilme[i]} | Diretor: {listaDiretorFilme[i]} | Ano de Lancamento: {listaAnoLancamentoFilme[i]} | Genero: {listaGeneroFilme[i]}")
  
def excluirFilmes():
    print("Certifique-se que sabe o numero do Indice do Livro ao qual deseja Apagar")
    
    confimacaoExcluirFilme=input('Deseja Continuar? (s/n): ')
    
    if confimacaoExcluirFilme == "s" or confimacaoExcluirFilme == "sim":
            indexFilmeExcluir = int(input('Insira o Indice do Filme a Excluir: '))
            listaTituloFilme.pop(indexFilmeExcluir)
            listaDiretorFilme.pop(indexFilmeExcluir)
            listaAnoLancamentoFilme.pop(indexFilmeExcluir)
            listaGeneroFilme.pop(indexFilmeExcluir)


while True:
    
    print("1 - Adicionar novo filme")
    print("2 - Procurar por título, diretor ou gênero")
    print("3 - Excluir filme")
    print("4 - Ordenar filmes")
    print("5 - Listar filmes")
    print("6 - Sair do Programa")
    userInputMenu=input("Escolha uma das opções anteriores: ")
    
    
    match userInputMenu:
        
        case "1":
            adicionarFilmes()
        case "2":
            procurarFilmes()
        case "3":
            excluirFilmes()
        case "4":
            ordenarFilmes()
        case "5":
            listarFilmes()
        case "6":
            print('A sair do programa!')
            break
        case _:
            print("----- INSIRA UM NUMERO DE 1 A 6!!! -----")
            
            