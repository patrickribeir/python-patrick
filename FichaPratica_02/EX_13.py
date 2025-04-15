vezes = int(input("Quantos números deseja inserir? "))

contador = 1
anterior = int(input("Digite o número: "))
crescente = True

while contador < vezes:
    atual = int(input("Digite o número: "))
    
    if atual < anterior:
        crescente = False
    
    anterior = atual
    contador += 1

if crescente:
    print("Os números estão em ordem crescente.")
else:
    print("Os números NÃO estão em ordem crescente.")
