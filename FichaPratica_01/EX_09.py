numero1 = int(input("Insira o numero 1: "))
numero2 = int(input("Insira o numero 2: "))
numero3 = int(input("Insira o numero 3: "))

if numero1 < numero2 and numero3:
    menor = numero1

elif numero2 < numero1 and numero3:
    menor = numero2

elif numero3 < numero1 and numero2:
    menor = numero3


print (f"O menor numero é: {menor}")
