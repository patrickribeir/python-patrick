salario = float(input("Digite o salário: "))
funcao= input("Digite o codigo do seu cargo: ")

if funcao == "101":
    print ("O seu salario atual é:", salario, "O valor do aumento será de 25%, que será: ", salario * 0.25, "O novo salario será: ", salario * 1.25)
elif funcao == "102":
    print ("O seu salario atual é:", salario, "O valor do aumento será de 20%, que será: ", salario * 0.20, "O novo salario será: ", salario * 1.20)
elif funcao == "103":
    print ("O seu salario atual é:", salario, "O valor do aumento será de 15%, que será: ", salario * 0.15, "O novo salario será: ", salario * 1.15)

else: 
    print ("O seu salario atual é:", salario, "O valor do aumento será de 10%, que será: ",  salario * 0.10 , "O novo salario será: ", salario * 1.10)

