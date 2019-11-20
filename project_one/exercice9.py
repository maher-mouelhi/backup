import random

number = random.randint(1,9)
guess = ""
count = 0
while guess != number and guess != "exit":

    guess = input("guess the nmmber or enter e to exit")

    if guess == "exit":
        print("bye bye")
        break

    count +=1
    guess = int(guess)
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("you are right the number is ",number)
        print("after  ",count,"tries")