def ler_valores_unicos(n):
    valores_unicos = set()
    lista_valores = []
    contador = 0

    while contador < n:
        try:
            valor = int(input(f"Digite o valor {contador + 1}: "))
            if valor not in valores_unicos:
                valores_unicos.add(valor)
                lista_valores.append(valor)
                contador += 1
            else:
                print("Valor repetido! Insira um valor diferente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    return lista_valores