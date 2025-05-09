# Função para multiplicar sem usar *
def multiplicar(a, b):
    resultado = 0
    contador = 0
    while contador < b:
        resultado += a
        contador += 1
    return resultado

# Programa principal
numero = int(input("Digite um número inteiro não-negativo: "))

while numero < 0:
    numero = int(input("Número inválido. Digite um número NÃO-NEGATIVO: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial = multiplicar(fatorial, contador)
    contador += 1

print(f"O fatorial de {numero} é {fatorial}")
