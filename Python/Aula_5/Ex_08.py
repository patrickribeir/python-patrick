import valid

while True:
    try:
        n = int(input("Quantos valores únicos deseja inserir? "))
        if n > 0:
            break
        else:
            print("Digite um número positivo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

valores = valid.ler_valores_unicos(n)
print("Valores únicos inseridos:", valores)
