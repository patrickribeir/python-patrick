numeros = []
print("Digite números inteiros e direi por ordem.")
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


for i in range(1, len(numeros) - 1):
    if numeros[i] > numeros[i - 1] and numeros[i] > numeros[i + 1]:
        print(numeros[i])