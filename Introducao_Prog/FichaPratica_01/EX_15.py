numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
ordem = str(input("crescente ou decrescente? "))

if numero1 < numero2 and numero1 < numero3:
    primeiro = numero1
    if numero2 < numero3:
        segundo = numero2
        terceiro = numero3
   
elif numero2 < numero1 and numero2 < numero3:
    primeiro = numero2
    if numero1 < numero3:
        segundo = numero1
        terceiro = numero3
       
elif numero3 < numero1 and numero3 < numero2:
    primeiro = numero3
    if numero2 < numero1:
        segundo = numero2
        terceiro = numero1
       

if ordem == "crescente":
 
    print(f"A ordem correta é: 1º: {primeiro}, 2º: {segundo}, 3º: {terceiro}")
    
elif ordem == "decrescente":
    print(f"A ordem correta é: 1º: {terceiro}, 2º: {segundo}, 3º: {primeiro}")

    

else:
    print("Digitos inválidos")