qntNumerosInseridos = 0
    

while qntNumerosInseridos < 50:
    numeroUserInput = int(input("Insira um numero entre 1 e 1000: "))
    
    if numeroUserInput >= 1 and numeroUserInput <= 1000:
        
        isPrime = True
        i=2
        while i < numeroUserInput:
            if numeroUserInput % i == 0:
                isPrime = False
            i+=1
            
        if numeroUserInput == 1:
            isPrime = False
        
        if isPrime == True:
            print(f"O numero {numeroUserInput} é primo!")
        else:
            print(f"O numero {numeroUserInput} não é primo!")
                
                
        
        
        
        
        if qntNumerosInseridos / 10 == 0.0:
            userContinue = input("Deseja Continuar? (sim/nao)")
            if userContinue == "nao" or userContinue == "Nao" or userContinue == "n":
                print("A sair")
                break
            else:
                continue
        

        
        
        qntNumerosInseridos+=1
    else:
        print('O numero que foi inserido é invalido.')
    
    
    
    

    

