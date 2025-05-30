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
 
print("\nNúmeros na lista:")
print(numeros)
 