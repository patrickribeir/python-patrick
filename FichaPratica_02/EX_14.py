numero = int(input("Digite um número inteiro não-negativo: "))

while numero < 0:
    numero = int(input("Número inválido. Digite um número NÃO-NEGATIVO: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print ("O valor fatorial é", fatorial)

