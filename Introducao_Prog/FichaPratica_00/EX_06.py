valor1 = int(input("Insira o num 1: "))
valor2 = int(input("Insira o num 2: "))

temp = valor1
valor1 = valor2
valor2 = temp

print(valor1, valor2)


valorX = int(input("Insira o num 1.1: "))
valorY = int(input("Insira o num 2.2: "))

valorX,valorY = valorY,valorX

print (valorX,valorY)
