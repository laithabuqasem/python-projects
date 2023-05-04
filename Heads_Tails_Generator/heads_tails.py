import random #imports module named: random

choice = input("Pick Heads or Tails: ").lower() #asks user to pick heads or tails
flip = random.randint(0, 1) #generates random number to pick heads or tails

if flip == 1: #if heads
    print("It was heads!")
    if choice == "heads":
        print(f"Great job! It was {choice} you got it right!")
    elif choice == "tails":
        print(f"You got it wrong! It's not {choice}.")
