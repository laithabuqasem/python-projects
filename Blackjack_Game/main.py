import random
# import os

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play == "y":
    # os.system('cls')
    print('\n' * 10)

    c1 = random.randint(1, 12)
    c2 = random.randint(1, 12)
    cc1 = random.randint(1, 12)

    print(f"Your cards: [{c1}, {c2}]")
    print(f"Computer's first card: {cc1}")
    next_card = input("Type 'y' to get another card, type 'n' to pass: ")
elif play == "n":
    print("Goodbye!")
else:
    print("Invalid input!")

"""
    Your cards: [9, 10]
    Computer's first card:
    Type 'y' to get another card, type 'n' to pass: 
"""