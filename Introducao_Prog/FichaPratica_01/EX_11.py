valorSaldo = float(input("Insira o seu saldo: "))
valorAMovimentar = float (input("Qual o montante do valor a movimentar? "))
operacao = str(input("Deseja depositar ou sacar? "))

if operacao == "depositar":
    saldoFin = valorSaldo + valorAMovimentar

elif operacao == "sacar":
    saldoFin = valorSaldo - valorAMovimentar

print (f"saldo final: {saldoFin}")

if saldoFin < 0:
    print ("O seu saldo esta negativo!")

else:
    print ("O seu saldo está positivo!")