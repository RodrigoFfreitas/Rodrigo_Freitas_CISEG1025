nota1 = 0 
nota2 = 0 
nota3 = 0 
peson1 = 2
peson2 = 3
peson3 = 5
media = 0

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 * peson1 + nota2 * peson2 + nota3 * peson3) / (peson1 + peson2 + peson3)

print(f"Media: {media}")  


if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

      