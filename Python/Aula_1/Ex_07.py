total_alunos = int(input("Quantos alunos tem na turma? "))
 
idades = []
 
for i in range(total_alunos):
    idade = int(input("Digite a idade do aluno: "))
    idades.append(idade)
 
idade_referencia = int(input("Verificar quantos têm mais de que idade? "))
 
contador_maiores = 0
for idade in idades:
    if idade > idade_referencia:
        contador_maiores += 1
 
percentagem = (contador_maiores / total_alunos) * 100
 
print("Percentagem de alunos com mais de", idade_referencia, "anos:", percentagem, "%")