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
 
impares = [n for n in numeros if n % 2 != 0]
 
if len(impares) == 0:
    print("Não há números ímpares na lista.")
else:
    media_impares = sum(impares) / len(impares)
    print(f"\nMédia dos números ímpares: {media_impares:.2f}")