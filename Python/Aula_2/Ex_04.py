frase = str(input("insira uma frase: "))

vogais = "aeiou"

contador = 0

for letra in frase:
    if letra.lower() in vogais:
        contador += 1 
       
        
print(f"Encontrei {contador} vogais dentro do texto")

# Imprimir ao contrario
print(frase[::-1])

palavrasDaFrase = frase.split()

print(" - " .join(palavrasDaFrase))

print ("".join(palavrasDaFrase))