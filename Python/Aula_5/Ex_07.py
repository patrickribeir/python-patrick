while True:
    try:
        n = int(input("Quantos valores deseja inserir? "))
        if n > 0:
            break
        else:
            print("Digite um número positivo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

valores = []
contador = 0
while contador < n:
    try:
        valor = int(input(f"Digite o valor {contador + 1}: "))
        valores.append(valor)
        contador += 1
    except ValueError:
        print("Valor inválido! Por favor, insira um número inteiro.")

i = 0
alterados = 0
while i < len(valores):
    if valores[i] < 0:
        valores[i] = 0
        alterados += 1
    i += 1

print("\nLista após substituir valores negativos por 0:")
print(valores)
print(f"Número total de valores alterados: {alterados}")
