def altura(lista_altura):
    contador = 0
    i = 0
    while i < len(lista_altura):
        if lista_altura[i] >= 1.50 and lista_altura[i] <= 1.75:
            contador += 1
        i += 1
    return contador

while True:
    try:
        n = int(input("Quantas pessoas você quer cadastrar? "))
        if n > 0:
            break
        else:
            print("Digite um número positivo.")
    except ValueError:
        print("insira um número inteiro válido.")

alturas = []
contador = 0
while contador < n:
    try:
        altura = float(input(f"Digite a altura da pessoa desejada: "))
        if altura > 0:
            alturas.append(altura)
            contador += 1
        else:
            print("A altura deve ser um número positivo.")
    except ValueError:
        print("Por favor, insira uma altura válida (ex: 1.70).")

quantidade = altura(alturas)
print(f"O número de pessoas com altura entre 1.50m e 1.75m é: {quantidade}")
