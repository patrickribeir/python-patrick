salario = float(input("Insira o valor do seu salario: "))

if salario <= 15000:  
    imposto = salario * 0.20


else:
    imposto = salario * 0.30

print (f"o valor do importo é: {imposto}")


