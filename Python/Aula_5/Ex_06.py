# Função para encontrar a soma mais comum
def soma_mais_comum(lista_lancamentos):
    frequencias = {}
    i = 0
    while i < len(lista_lancamentos):
        dado1, dado2 = lista_lancamentos[i]
        soma = dado1 + dado2
        if soma in frequencias:
            frequencias[soma] += 1
        else:
            frequencias[soma] = 1
        i += 1

    mais_comum = None
    maior_frequencia = 0

    for soma in frequencias:
        if frequencias[soma] > maior_frequencia:
            maior_frequencia = frequencias[soma]
            mais_comum = soma

    return mais_comum

# Pedir número de lançamentos
while True:
    try:
        n = int(input("Quantos lançamentos deseja inserir? "))
        if n > 0:
            break
        else:
            print("Digite um número positivo.")
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")

# Ler os lançamentos manualmente
lancamentos = []
contador = 0
while contador < n:
    try:
        dado1 = int(input(f"Lançamento {contador+1} - valor do dado 1: "))
        dado2 = int(input(f"Lançamento {contador+1} - valor do dado 2: "))
        
        if dado1 < 1 or dado1 > 6 or dado2 < 1 or dado2 > 6:
            print("Os dados devem ter valores entre 1 e 6.")
        else:
            lancamentos.append((dado1, dado2))
            contador += 1

    except ValueError:
        print("Por favor, insira apenas números inteiros.")

# Calcular e exibir a soma mais comum
resultado = soma_mais_comum(lancamentos)
print(f"\nA soma mais comum dos dados foi: {resultado}")