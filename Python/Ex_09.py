contador = 0
soma = 0
 
while contador < 5 or soma <= 100:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    contador += 1
 
print("Você digitou", contador, "números com soma", soma)

