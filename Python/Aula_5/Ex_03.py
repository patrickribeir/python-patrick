def idade_mais_velha(lista_idades):
    i = 0
    maisvelho = lista_idades[0]
    while i < len(lista_idades):
        if lista_idades[i] > maisvelho:
            maisvelho = lista_idades[i]
        i += 1
    return maisvelho


while True:
    try:
        numAlunos = int(input("Quantos alunos há na turma? "))
        if numAlunos > 0:
            break
        else:
            print("O número de alunos deve ser positivo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

idades = []
contador = 0
while contador < numAlunos:
    try:
        idade = int(input(f"Digite a idade do aluno {contador + 1}: "))
        if idade >= 0:
            idades.append(idade)
            contador += 1
        else:
            print("A idade não pode ser negativa.")
    except ValueError:
        print("Por favor, insira uma idade válida.")

mais_velho = idade_mais_velha(idades)
print(f"\nA idade mais velha é: {mais_velho}")
