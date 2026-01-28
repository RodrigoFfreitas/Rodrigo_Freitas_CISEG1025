

userInput = int(input("Insira um numero entre 1 e 1000: "))
isPrime = True


if userInput >= 1 and userInput <=1000:
    i=2
    while i > userInput:
        
        if userInput == 1:
            isPrime = False        
        elif userInput % i == 0:
            isPrime = False

            
        i+=1
        
    if isPrime == True:
        print(f"O numero {userInput} é primo")
    elif isPrime == False:
        print(f"O numero {userInput} não é primo")

else:
    print("Deve inserir um numero entre 1 e 1000")       