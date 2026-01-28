num = int(input("Insira um numero inteiro para verificar se é primo ou não.\n"))
i=2
primo = True

while i < num:
    
    if num % i == 0:
        primo = False
        break
    i += 1

if primo == True:
    print("O numero inserido é primo")
else:
    print("O numero inserido não é primo")
    
        
    