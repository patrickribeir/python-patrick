#Asks the user for the number he/she wants to see if is prime number
number=int(input("Insert a number see if is prime number."))
count=2

#Verifies if the number is prime number or not and prints the result.
#Prime number is a number that is only divisible by 1 and itself

while count<=number:
    if number%count==0:
        if number==count:
            print("Number",number,"is a prime number!")
            break
        else:
            print("Number",number,"isn't a prime number!")
            break
    else:
        count+=1    

#Or you can do this
for i in number:
    if number%count==0:
        if number==count:
            print("Number",number,"is a prime number!")
            break
        else:
            print("Number",number,"isn't a prime number!")
            break
    else:
        count+=1    