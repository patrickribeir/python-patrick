soma = 0
quantidade = 0
 
numero = float(input("Digite um número (0 para parar): "))
 
while numero != 0:
    soma += numero
    quantidade += 1
    numero = float(input("Digite um número (0 para parar): "))
 
# Verificando se pelo menos um número foi digitado0
if quantidade > 0:
    media = soma / quantidade
    print("Soma dos números:", soma)
    print("Média dos números:", media)
else:
    print("Nenhum número foi digitado.")