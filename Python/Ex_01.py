saldoM = float(input("Digite o saldo medio: "))

if saldoM <= 200:
    print(f"O seu saldo é {saldoM} Nenhum credito disponivel")
elif saldoM <= 400:
    print(f"O seu saldo é {saldoM}, O valor do credito disponivel são 20% sobre o seu saldo medio, que será: ", saldoM * 0.20)
elif saldoM <= 600:
    print(f"O seu saldo é {saldoM}, O valor do credito disponivel são 30% sobre o seu saldo medio, que será: ", saldoM * 0.30)
elif saldoM > 600:
    print(f"O seu saldo é {saldoM}, O valor do credito disponivel são 40% sobre o seu saldo medio, que será: ", saldoM * 0.40)


