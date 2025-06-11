

#Crie um programa em Python que solicite ao utilizador a introdução de 10 valores inteiros,
#armazene-os numa lista, e apresente os seguintes resultados no ecrã:
numeros = []
negativo = 0
positivo = 0


while True:
    try:
        
        for i in range(10):
            numero = int(input("Insira um número inteiro: "))
            numeros.append(numero)
            if numero < 0:
                negativo += 1

        
        break
        

    except ValueError:
        print("Por favor, insira apenas números inteiros.")



#Contabilizar o número de valores que são negativos;


print ("quantidade de numeros negativos:", negativo)


#Calcular a média dos valores positivos inseridos;

positivo = [n for n in numeros if n > 0]

if positivo:
    media = sum(positivo) / len(positivo)

    print("a media dos numeros positivo : ", media)

else:
    print ("Nenhum numero positivo foi inserido")

#Identificar os valores que são múltiplos de 3 e de 5 em simultâneo.

print("Multiplos de 3 e 5: ",[n for n in numeros if n % 3 == 0 and n % 5 == 0])
 