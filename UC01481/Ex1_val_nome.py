nomeUser = input('Insira o seu nome: ')

if len(nomeUser) == 0:
    print("Nome Inválido!")
    exit()



if not 65 <= (ord(nomeUser[0])) <= 90:
    print("Nome Inválido!")
    exit()
    
    
for i in range(len(nomeUser)):
    
    nCodAscii = ord(nomeUser[i])
    
    if nCodAscii == 32:
        if i == len(nomeUser) - 1:
            print("Nome Inválido!")
            exit()
        
        if not 65 <= ord(nomeUser[i + 1]) <= 90:
            print("Nome Inválido!")
            exit()
    
    elif 65 <= nCodAscii <= 90:
        if i != 0 and ord(nomeUser[i - 1]) != 32:
            print("Nome Invalido!")
            exit()
    
    elif 97 <= nCodAscii <= 122:
        pass
    
    else:
        print('Nome Inválido!')
        exit()
        
    
print('Nome Válido!!')
                
            

            