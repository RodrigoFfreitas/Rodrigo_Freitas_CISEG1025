nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
nota6 = 0
nota7 = 0
nota8 = 0
nota9 = 0
nota10 = 0
notasAcimaouIgualMedia = 0

nota1 = float(input("Insira a nota do aluno 1: "))
nota2 = float(input("Insira a nota do aluno 2: "))
nota3 = float(input("Insira a nota do aluno 3: "))
nota4 = float(input("Insira a nota do aluno 4: "))
nota5 = float(input("Insira a nota do aluno 5: "))
nota6 = float(input("Insira a nota do aluno 6: "))
nota7 = float(input("Insira a nota do aluno 7: "))
nota8 = float(input("Insira a nota do aluno 8: "))
nota9 = float(input("Insira a nota do aluno 9: "))
nota10 = float(input("Insira a nota do aluno 10: "))

# Cálculo da média
media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10) / 10

print(f"Média da turma: {media}")





if nota1 >= media:
    notasAcimaouIgualMedia += 1
if nota2 >= media:
    notasAcimaouIgualMedia += 1
if nota3 >= media:
    notasAcimaouIgualMedia += 1
if nota4 >= media:
    notasAcimaouIgualMedia += 1
if nota5 >= media:
    notasAcimaouIgualMedia += 1
if nota6 >= media:
    notasAcimaouIgualMedia += 1
if nota7 >= media:
    notasAcimaouIgualMedia += 1
if nota8 >= media:
    notasAcimaouIgualMedia += 1
if nota9 >= media:
    notasAcimaouIgualMedia += 1
if nota10 >= media:
    notasAcimaouIgualMedia += 1

print(f"Alunos com nota igual ou acima da média: {notasAcimaouIgualMedia}")