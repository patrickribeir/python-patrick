x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
 
# Verifica qual é o menor numero e o maior, para contar certinho, em ordem crescente
inicio = min(x, y)
fim = max(x, y)
 
print("Números pares entre", inicio, "e", fim, ":")
 
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)