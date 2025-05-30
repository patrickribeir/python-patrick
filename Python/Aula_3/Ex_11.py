numeros = []
 
print("Digite números inteiros para a lista.")
print("Digite 'sair' para encerrar.\n")
 
while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
 
numeros.sort()
 
print("\nLista ordenada em ordem crescente:")
for n in numeros:
    print(n)
 