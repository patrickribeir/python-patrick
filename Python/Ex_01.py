saldoM = float(input("Digite o saldo mensal: "))

if saldoM <= 200:
    print("Nenhum credito disponivel")
elif saldoM <= 400:
    print("O valor do credito disponivel são 20% sobre o seu saldo medio, que será: ", saldoM * 0.20)
elif saldoM <= 600:
    print("O valor do credito disponivel são 30% sobre o seu saldo medio, que será: ", saldoM * 0.30)
elif saldoM > 600:
    print("O valor do credito disponivel são 40% sobre o seu saldo medio, que será: ", saldoM * 0.40)


