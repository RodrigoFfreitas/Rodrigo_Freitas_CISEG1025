#################  Listas  #####################

listaVazia=[]
listanum=[1,4,5,6,9]
listaString=['Pedro','Joao','Rui']
listaMista=["ola",2,True]
texto="Eu gosto de Python"
texto="Eu adoro Pizza"

# NÃO ESQUECER QUE O INDEX DAS LISTAS COMEÇA PELO 0, ou seja para aceder ao primeiro dado usamos o item 0, e aceitam todos os tipos de dados anteriores

print(type(listaMista))
print(listanum)
listanum.insert(0,9)  #neste caso usamos a função insert com o index 0 para adicionar o valor 9 e empurar o resto para a frente | desta maneira tmb dá mas pode nao funfa em versões mais antigas listanum[0]=9
print(f"Depois de usar o metodo insert {listanum}")
listanum.pop(1) # vai apagar o numero que esta a frente do novo numero inserido, ou seja o 1 que foi arrastado para a frente vai ser apagado | apaga o valor que está no index indicado
print(listanum)
listanum.append(11) # adiciona um numero no fim da lista
print(listanum)
listanum.remove(9)  # remove o primeiro elemento da lista que tenha o valor desejado
print(listanum)
listanum.reverse() # Inverte a lista toda
print(listanum)
listanum.insert(0,9) # apenas para desordenar a lista
print(listanum)
listanum.sort()  # vai organizar a lista, neste caso por ordem crescente
print(listanum)



listaSplit=texto.split(" ")   # a lista sera igual ao conteudo da var texto, separada por aquilo que desejamos, neste caso por espaços mas podemos em vez de espaços podemos separar por uma palavra por exemplo
print(listaSplit)


#################  Tuplas  #####################

# as tuplas são constantes, ou seja, são listas normas mas sempre fixas
tupla=()
tupla=(1,2)
#tupla[0]=3  isto da erro!
tuplaextentions=(".mp3", ",jpeg",".docs")
print(tupla)
print(tuplaextentions[1])


opc1=input('Escolha a opção desejada')
opc2=input('Escolha outra opção desejada')

tuplaescolha=(opc1,opc2) # tupla dinamica, ou seja recebe os dados do user, MAS ja não pode ser alterada a partir daqui
                         # ou seja a tupla não necessita de ser declarada por valores conhecido, e pode receber dados vindos do user

print(tuplaescolha)



#################  Loops  #####################
#################  for  #####################


# os loops funciona da seguinte forma: enquanto a condição for verdadeira executa

listanum=[1,6,3,9,4,8,3]

# foreache com variavel nas posicoes todas da lista

for posicaolista in listanum:
    print(posicaolista)  # o output disto será o conteudo da lista por ordem de index
    

print("tamanho da lista", len(listanum)) # mostra o tamnho da lista



# foreache para indexar ou criar numeros de qualquer range

for i in range(len(listanum)): # isto vai fazer o for pela duração ou seja o conteudo da lista
    print(listanum[i])
    
    
print("saltar no index da lista de 2 em 2")
for i in range(0,7,2): # isto vai fazer o for da duração da lista saltando de 2 em 2
    print(listanum[i])


for i in range (1,20): # o range quando nao tem o primeiro valor ele vai comecar sempre em 0
    print(i)

print("range igual ao anterior mas a pular de 3 em 3")    

for i in range (1,20,3): # mesma coisa que antes mas de 3 em 3
    print(i)
    


 
 
#################  Loops  #####################
#################  while  #####################

listanum=[1,6,3,9,4,8,3]

i=0 

while i < len(listanum):
    print("elemento:", listanum[i] , " posição index", i)
    i+=1
    
# mesma coisa que o while anterior, mas de 2 em 2
while i < len(listanum):
    print("elemento:", listanum[i] , " posição index", i)
    i+=2


it=1

while it<=20:
    print(it)
    if it == 10:
        break
    it+=1 

    
    
it=0

while it<=20:
    it+=1
    if it == 10:
        continue
    print(it)

