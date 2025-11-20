#
# Não entendi o que o professor pediu neste exercicio, por isso fiz uma versão que lê um numero de um user e responde se é perfeito ou não
# E outro que lê um numero dado pelo user, e verifica se existe algum numero perfeiro no intrevalo de 1 até ao numero inserido
#

# Versão verificar se numero inserido é perfeito ou não

num = int(input("Insira um numero inteiro: "))
soma = 0
i = 1
while i < num:
    if num % i == 0:
        soma += i
    
    i += 1
    
if soma == num:
    print(f"O numero {num} é um numero perfeito")
else:
    print(f"O numero {num} não é um numero perfeito")


    
# Versão verificar se existe algum numero perfeito no intrevalo entre 1 e num

intervalo = int(input("Insira um numero inteiro: "))

cont_nperf = 0
num = 1

while num <= intervalo:
    soma = 0
    i = 1

    while i < num:
        if num % i == 0:
            soma += i
        i += 1

    if soma == num:
        print(f"{num} é um numero perfeito")
        cont_nperf += 1

    num += 1

print(f"Existem {cont_nperf} numeros perfeitos entre 1 e {intervalo}.")
