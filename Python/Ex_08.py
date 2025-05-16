contador_impares = 0
maior_par = None
 
while contador_impares < 5:
    numero = int(input("Digite um número inteiro: "))
 
    if numero % 2 == 0:
        if maior_par is None or numero > maior_par:
            maior_par = numero
    else:
        contador_impares += 1
 
if maior_par == 0:
    print("Nenhum número par foi digitado.")
else:
    print(f"O maior número par digitado foi é {maior_par}")