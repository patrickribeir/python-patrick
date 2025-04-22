count=1

#Asks the user number 1 for the number to guess
numberToGuess=int(input("What number do you want player 2 to guess?"))

#Will continue until the user 2 finds what the number is and tell how many tries it required to guess.


for i in range(100000):
    numberGuessed=int(input("What is the number you want to try?"))

    if numberGuessed!=numberToGuess:
        print("Wrong answer! Try again!")
        count+=1
    else:
        print("You got it! The number is",numberGuessed,".\nYou needed",count,"tries to guess the correct number!")
        break

#Or can do this
""" while True:
    numberGuessed=int(input("What is the number you want to try?"))

    if numberGuessed!=numberToGuess:
        print("Wrong answer! Try again!")
        count+=1
    else:
        print("You got it! The number is",numberGuessed,".\nYou needed",count,"tries to guess the correct number!")
        break """