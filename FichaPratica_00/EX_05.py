numero1 = float(input("numero 1: "))
numero2 = float(input("numero 2: "))
numero3 = float(input("numero 3: "))

mediaAri = (numero1+numero2+numero3) / 3
mediaPon = (numero1*0.20) + (numero2*0.30) + (numero3*0.50) / (0.20+0.30+0.50)

print("Media Aritimetica", mediaAri)
print("Media Ponderada", mediaPon)