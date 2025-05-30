
L1 = []

print("Digite os números inteiros para a lista L1.")

print("Digite 'sair' para encerrar.\n")
 
while True:

    entrada = input("L1 - Digite um número: ")

    if entrada.lower() == 'sair':

        break

    try:

        numero = int(entrada)

        L1.append(numero)

    except ValueError:

        print("Por favor, digite um número inteiro válido.")
 

L2 = []

print("\nDigite os números inteiros para a lista L2.")

print("Digite 'sair' para encerrar.\n")
 
while True:

    entrada = input("L2 - Digite um número: ")

    if entrada.lower() == 'sair':

        break

    try:

        numero = int(entrada)

        L2.append(numero)

    except ValueError:

        print("Por favor, digite um número inteiro válido.")
 


comuns = list(set(L1) & set(L2))
 


print("\nLista L1:", L1)

print("Lista L2:", L2)
 
if comuns:

    print("\nElementos comuns às duas listas:")

    print(comuns)

else:

    print("\nNão há elementos comuns entre as listas.")