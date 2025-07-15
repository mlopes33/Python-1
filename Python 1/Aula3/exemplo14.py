#Nota do aluno
nota = float(input("Digite sua nota"))
if(nota>=7):
    print("Aprovado!")
elif(nota>=5 and nota<=6.9):
    print("Você está de recuperação!")
else:
    print("Preprovado")