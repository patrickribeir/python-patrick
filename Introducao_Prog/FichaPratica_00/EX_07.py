prod1 = float(input("Valor do 1 prod: "))
prod2 = float(input("Valor do 2 prod: "))
prod3 = float(input("Valor do 3 prod: "))

valorTotal = (prod1+prod2+prod3)

valorDesc = (valorTotal*0.10)

ValorAPagar = valorTotal-valorDesc

print ("valor a Pagar: ", ValorAPagar)