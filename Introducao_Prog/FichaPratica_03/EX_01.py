cont="y"




for i in range(1000000000):
    #Asks what the operation that it wants to do. If invalid gives and error
    operation=input("Please tell what operation you want to do\n" \
    "+ - Sum\n" \
    "- - Subtraction\n" \
    "/ - Division\n" \
    "* - Multiplication.\n"
    "N . Exit\n")

    if operation!="N":
        #Asks the user for two real numbers
        number1=float(input("Insert the first number: "))
        number2=float(input("Insert the second number: "))
        
        #Does the operation and if valid presents the result. Asks if the user wants to do another calculation
        if operation=="+":
            result=number1+number2
            print("\nThe result of",number1,"+",number2,"=",result,"\n")
        elif operation=="-":
            result=number1-number2
            print("\nThe result of",number1,"-",number2,"=",result,"\n")
        elif operation=="/":
            if number2==0:
                print("\nCan't divide by zero!\n")
            else:
                result=number1/number2
                print("\nThe result of",number1,"/",number2,"=",result,"\n")
        elif operation=="*":
            result=number1*number2
            print("\nThe result of",number1,"*",number2,"=",result,"\n")
        else:
            print("Invalid operation selection!")

    else:
        break
    
#Or you can do this
""" while cont=="y":
    #Asks the user for two real numbers
    number1=float(input("Insert the first number: "))
    number2=float(input("Insert the second number: "))
    #Asks what the operation that it wants to do. If invalid gives and error
    operation=input("Please tell what operation you want to do\n" \
    "+ - Sum\n" \
    "- - Subtraction\n" \
    "/ - Division\n" \
    "* - Multiplication.\n")

    #Does the operation and if valid presents the result. Asks if the user wants to do another calculation
    if operation=="+":
        result=number1+number2
        print("The result of",number1,"+",number2,"=",result)
    elif operation=="-":
        result=number1-number2
        print("The result of",number1,"-",number2,"=",result)
    elif operation=="/":
        if number2==0:
            print("Can't divide by zero!")
        else:
            result=number1/number2
            print("The result of",number1,"/",number2,"=",result)
    elif operation=="*":
        result=number1*number2
        print("The result of",number1,"*",number2,"=",result)
    else:
        print("Invalid operation selection!")

    cont=input("Do you want to continue?\n(Y/N)").strip().lower() """