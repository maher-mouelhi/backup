#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import random
list = ["R","S","P"]
choix = ""

while choix != "Q":
    choix = str(input("Enter your choice R: Rock,S: Scissors,P: Paper or Q to quit:  "))
    computer = random.choice(list)
    print(computer)
    if choix == "R" and computer == "S" or choix == "S" and computer == "P" or choix == "P" and computer == "R":
        print("you win ! :) ")
        break
    elif computer == "R" and choix == "S" or computer == "S" and choix == "P" or computer == "P" and choix == "R":
        print("you lose :( ! ")
        break
    elif computer == choix:
        print("equal ! ")
        break
    elif choix == "Q":
        print("bye bye! ")
        break
    else:
        print("wrong try again ! ")
