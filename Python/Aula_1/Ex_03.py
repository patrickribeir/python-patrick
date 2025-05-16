alunos = int (input ("Quantos alunos existe na turma? "))

somadenotas = 0

for i in range (alunos):
       
        nota = float (input("Digite a nota do aluno: "))
        somadenotas += nota

 #media aritmetica da tuma

media = somadenotas / (alunos)
print ("A media da turma é: ", media)   