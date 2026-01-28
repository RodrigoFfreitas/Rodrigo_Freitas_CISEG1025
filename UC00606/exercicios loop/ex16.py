i=0
total= 0

while i < 30:
    num=int(input("Insira um numero par entre 1 e 50, para calcular a media\n"))
    
    if num % 2 == 0 and num <= 50 and num >= 1:
        total += num
        i += 1
    else:
        print(f"O numero {num} não está entre 1 e 50 ou não é par\n")
    


media = total / 30

print(f"A Média dos numeros inseridos é: {media}")
    
