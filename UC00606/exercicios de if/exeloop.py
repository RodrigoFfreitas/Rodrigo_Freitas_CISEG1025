numero = 0
npar=0
nimpar=0

for i in range(10):
    numero = int(input("Insira um numero inteiro: "))
    
    if numero % 2 == 0:
        npar += 1
    else:
        nimpar += 1
        
    print(f"Pares: {npar}\nImpares: {nimpar}")
    
    