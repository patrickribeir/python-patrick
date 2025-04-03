musc1min = float(input("Insira a 1 musica em min: "))
musc1seg = float(input("Insira a 1 musica em seg: "))
musc2min = float(input("Insira a 2 musica em min: "))
musc2seg = float(input("Insira a 2 musica em seg: "))
musc3min = float(input("Insira a 3 musica em min: "))
musc3seg = float(input("Insira a 3 musica em seg: "))
musc4min = float(input("Insira a 4 musica em min: "))
musc4seg = float(input("Insira a 4 musica em seg: "))
musc5min = float(input("Insira a 5 musica em min: "))
musc5seg = float(input("Insira a 5 musica em seg: "))
#Transformaçao de todos os minutos em segundos
valorDosMinsEmSeg = (musc1min + musc2min + musc3min + musc4min + musc5min) * 60
# soma dos valores dos mins convertidos em seg + a soma dos segundos ja existentes
valorTotalSeg = valorDosMinsEmSeg + musc1seg + musc2seg + musc3seg + musc4seg + musc5seg
#valor total em segundos divididos por horas, para descobrir quantas horas cabem dentro do total de segundos
totalHoras = int(valorTotalSeg / 3600)
#usamos % para saber quantos mins cabem dentro dos seg restantes. 
totalMins = int((valorTotalSeg % 3600) / 60)
# % novamente para descobrir o valor restante em, minutos
totalSeg = int (valorTotalSeg % 60)
#para o programa rodar, tive que add str na frente de resultado numerico para tornar uma string.
print (str(totalHoras) + "H" + str(totalMins) + "m" + str(totalSeg) + "s")

