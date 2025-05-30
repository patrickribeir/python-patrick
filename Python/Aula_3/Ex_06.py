numeros = []
print("Digite números inteiros para adicionar à lista.")
print("Digite 'sair' para encerrar.")
 
while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
 
if len(numeros) < 2:
    print("A lista precisa ter pelo menos 2 números para calcular a diferença.")
else:
    maior_diferenca = 0
 
    for i in range(len(numeros) - 1):
        diferenca = abs(numeros[i] - numeros[i + 1])
        if diferenca > maior_diferenca:
            maior_diferenca = diferenca
 
    print(f"\nMaior diferença entre dois itens consecutivos: {maior_diferenca}")