totalnotas=0

for i in range(10):
    nota=float(input("Insira uma nota: "))
    totalnotas=totalnotas + nota
    
    if i == 9:
        media=totalnotas/10
        print("Media das notas:", media)
