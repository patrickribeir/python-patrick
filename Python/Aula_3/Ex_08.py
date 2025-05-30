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
 
multiplos_de_3 = [n for n in numeros if n % 3 == 0]
 
if not multiplos_de_3:
    print("Não há múltiplos de 3 na lista.")
else:
    print("\nNúmeros múltiplos de 3:")
    print(multiplos_de_3)