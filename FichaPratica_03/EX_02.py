option="0"

for i in range(100000000):
    #Asks the user to choose the option
    option=input("Select an option from the Menu:\n1 - Create\n2 - Update\n3 - Delete\n4 - Exit\n")

    #If invalid informs with an error
    if option=="1":
        print("Menu Create")
    elif option=="2":
        print("Menu Update")
    elif option=="3":
        print("Menu Delete")
    elif option=="4":
        print("Exit")
        break
    else:
        print("Invalid Option!")

#Or you can do this
""" while option!="4":
    #Asks the user to choose the option
    option=input("Select an option from the Menu:\n1 - Create\n2 - Update\n3 - Delete\n4 - Exit\n")

    #If invalid informs with an error
    if option=="1":
        print("Menu Create")
    elif option=="2":
        print("Menu Update")
    elif option=="3":
        print("Menu Delete")
    elif option=="4":
        print("Exit")
    else:
        print("Invalid Option!") """