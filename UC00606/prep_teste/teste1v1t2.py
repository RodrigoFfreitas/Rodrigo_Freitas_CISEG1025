

listaLivro=[]
listaAutor=[]
listaAnoPub=[]
userInput=''


def cadastrarLivros():
    print("Insira o nome do livro que deseja adicionar!")
    listaLivro.append(input())
    
    print("Insira o Nome do Autor do Livro que deseja adicionar!")
    listaAutor.append(input())
    
    print("Insira o ano do Livro que deseja adicionar!")
    listaAnoPub.append(input())

def excluirLivro():
    desejaContinuar = input('Para Excluir um livro tem de saber qual o seu index, deseja continuar? (s/n)')
    
    if desejaContinuar.lower == 's' or desejaContinuar.lower == 'sim':
        indexLivroExcluir = int(input('Insira o Indice do Livro a Excluir: '))
        listaLivro.pop(indexLivroExcluir)
        listaAutor.pop(indexLivroExcluir)
        listaAnoPub.pop(indexLivroExcluir)



while True:
    print('1 - Cadastrar Livros')
    print('2 - Procurar por Livros')
    print('3 - Excluir Livros')
    print('4 - Ordenar Livros')
    print('5 - Listar todos os Livros Cadastrados')
    print('6 - Sair')
    userInput=input('Escolha uma das opções anteriores: ')
    
    match userInput:
        case '1':
            cadastrarLivros()
        case '2':
            print('opc 2 selecionada')
        case '3':
            excluirLivro()
        case '4':
            print('opc 4 selecionada')
        case '5':
            print('opc 5 selecionada')
        case '6':
            print('A Sair do Programa!')
            break
        case _:
            print("Escolha uma opção válida!")

