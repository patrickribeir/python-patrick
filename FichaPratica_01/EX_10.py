numero1 =  float(input ("Insira o primeiro numero: "))
numero2 = float(input("insira o segundo numero: "))
operacao = str (input("Insira o simbolo da operação que deseja"))

if operacao == "+":
    resultado = numero1 + numero2
    print (f"O resultado é: {resultado}")

elif operacao == "-":
    resultado = numero1 - numero2
    print (f"O resultado é: {resultado}")

elif operacao == "/":
    resultado = numero1 / numero2
    print (f"O resultado é: {resultado}")

elif operacao == "*":
    resultado = numero1 * numero2
    print (f"O resultado é: {resultado}")

else: 
    print ("ERRO! Insira algum dos seguintes simbolos + - / ou *")

