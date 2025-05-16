alunos = int(input("insira a quantidade de alunos: ")) 

positivo = 0
negativo = 0

for i in range(0, alunos):
    nota = float(input("insira a nota do aluno: "))
    
    if nota >= 0:
        positivo += 1
    else:
        negativo += 1

print("A quantidade de alunos com nota positiva é: ", positivo)
print("A quantidade de alunos com nota negativa é: ", negativo)