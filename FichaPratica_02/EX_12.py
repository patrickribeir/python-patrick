vezes = int(input("Quantos números deseja inserir? "))
numeros = []  # Lista para guardar os números

# Ler os números
contador = 0
while contador < vezes:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    contador += 1

# Verificar se está em ordem crescente
crescente = True
for i in range(1, len(numeros)):
    if numeros[i] < numeros[i - 1]:  # Se algum número for menor que o anterior
        crescente = False
        break

if crescente:
    print("Os números estão em ordem crescente.")
else:
    print("Os números NÃO estão em ordem crescente.")
