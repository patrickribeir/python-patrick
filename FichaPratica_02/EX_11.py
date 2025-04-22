
number=0
interval0_25=0
interval26_50=0
interval51_75=0
interval76_100=0
  
#Asks the user for a number and if the number is negative it ends
#Sees in what interval these number is in and prints
while number>=0:
    number=int(input("Insert a number from 0 to 100. To finish enter a negative number: "))
    print(number)
    if number>=0 and number<=25:
        interval0_25+=1
    elif number>=26 and number<=50:
        interval26_50+=1
    elif number>=51 and number<=75:
        interval51_75+=1
    elif number>=76 and number<=100:
        interval76_100+=1
    else:
        print("The number is outside the defined interval!")
      
print("[00, 25]: ",interval0_25,"\n[26, 50]: ",interval26_50,"\n[51, 75]: ",interval51_75,"\n[76, 100]: ",interval76_100)