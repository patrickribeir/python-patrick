
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
 

from collections import Counter
 
contagem_L1 = Counter(L1)
contagem_L2 = Counter(L2)
 
comum_total = []
 
for elemento in contagem_L1:
    if elemento in contagem_L2:
      
        total_ocorrencias = contagem_L1[elemento] + contagem_L2[elemento]
        
        comum_total.extend([elemento] * total_ocorrencias)
 
if comum_total:
    print("\nElementos comuns (imprimidos todas as vezes que aparecem nas duas listas):")
    for x in comum_total:
        print(x)
else:
    print("\nNão há elementos comuns entre as listas.")