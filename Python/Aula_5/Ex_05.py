def nif(lista_nifs, nif_procurado):
    i = 0
    while i < len(lista_nifs):
        if lista_nifs[i] == nif_procurado:
            return i
        i += 1
    return -1  

while True:
    try:
        n = int(input("Quantos NIFs você deseja inserir? "))
        if n > 0:
            break
        else:
            print("Por favor, insira um número positivo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

nifs = []
contador = 0
while contador < n:
    try:
        nif = int(input(f"Digite o NIF da pessoa {contador + 1}: "))
        nifs.append(nif)
        contador += 1
    except ValueError:
        print("Por favor, insira um NIF válido (apenas números inteiros).")

while True:
    try:
        nif_pesquisa = int(input("Digite o NIF que deseja pesquisar: "))
        break
    except ValueError:
        print("Por favor, insira um NIF válido.")

posicao = nif(nifs, nif_pesquisa)

if posicao != -1:
    print(f"\nO NIF {nif_pesquisa} foi encontrado na posição {posicao} da lista.")
else:
    print(f"\nO NIF {nif_pesquisa} não foi encontrado na lista. :()")