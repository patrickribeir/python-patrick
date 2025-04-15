
for _ in range (100):

    num1= int(input("insira o 1 numero: "))
    num2= int(input("insira o 2 numero: "))
    operacao = input("qual operacao deseja, filho? (+ - * /): ")
    continuar = input("continuar a operacao: (S = sair / C = continuar")

    if continuar == "s":
        print ("Obrigado")
        break
    if continuar == "c":
        continue

    if operacao == "+":
            print num1 + num2
    elif operacao == "-":
            resultado = num1 - num2
    elif operacao == "*":
            resultado = num1 * num2
    elif operacao == "/":
            if num2 == 0:
                print("Erro: Divisão por zero não permitida!")
                continue
            resultado = num1 / num2
    else:
            print("Operação inválida. Tente novamente.")
            continue
    
    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")


