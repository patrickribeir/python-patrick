#Crie um programa em Python que leia duas horas completas (hora de entrada e hora de saída de
#um funcionário), e calcule o tempo total em que esse funcionário esteve a trabalhar. Para isso:
 #1-Solicite ao utilizador que insira 3 valores inteiros (hora, minuto e segundo) para representar a
#hora de entrada e a hora de saída;

#2-Crie uma função que receba os 3 valores (hora, minuto e segundo) como parâmetros, e
#converta tudo para segundos, retornando esse valor;
def horario(hora, minuto, segundo):
    return hora * 3600 + minuto * 60 + segundo
 
horaE = int(input("Informe sua hora de entrada: "))
minutoE = int(input("Informe seu minuto de entrada: "))
segundoE = int(input("Informe seu segundo de entrada: "))
 
horaS = int(input("Informe sua hora de saída: "))
minutoS = int(input("Informe seu minuto de saída: "))
segundoS = int(input("Informe seu segundo de saída: "))
 
entrada_segundos = horario(horaE, minutoE, segundoE)
saida_segundos = horario(horaS, minutoS, segundoS)
 
tempo_total = saida_segundos - entrada_segundos
 
print(f"Tempo total em segundos: {tempo_total}")


 
#Crie uma nova função que receba esse intervalo (em segundos) e converta-o para o formato
#HH:MM:SS, apresentando o resultado final no ecrã.


horas = tempo_total // 3600
minutos = (tempo_total % 3600) // 60
segundos = tempo_total % 60
 
print(f"Tempo total de trabalho: {horas:02d}:{minutos:02d}:{segundos:02d}")

