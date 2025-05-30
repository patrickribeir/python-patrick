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
 
print (" o maior número é:", max(numeros))
print (" o menor número é:", min(numeros))
