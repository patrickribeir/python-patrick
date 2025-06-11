def ler_lista_inteiros(n):
    lista = []
    contador = 0
    while contador < n:
        try:
            valor = int(input(f"Digite o valor {contador + 1}: "))
            lista.append(valor)
            contador += 1
        except ValueError:
            print("Entrada inválida! Insira um número inteiro.")
    return lista

def segundo_maior(lista):
    valores_distintos = set(lista)

    if len(valores_distintos) < 2:
        return "Erro: não existem pelo menos dois valores distintos na lista."

    maior = max(valores_distintos)
    valores_distintos.remove(maior)

    segundo = max(valores_distintos)
    return segundo
