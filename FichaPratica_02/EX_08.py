
number=0
sum=0
count=0

while True:
    number=int(input("Insert a number. If you want to exit type -1: "))
    if number==-1:
        average=sum/count
        print("The average is:",average)
        break
    else:
        sum+=number
        count+=1