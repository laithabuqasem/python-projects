import random
# import os

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if play == "y":
    # os.system('cls')
    print('\n' * 10)

    c1 = random.randint(1, 12)
    c2 = random.randint(1, 12)
    c3 = random.randint(1, 12)
    cc1 = random.randint(1, 12)
    cc2 = random.randint(1, 12)
    cfinal = c1 + c2
    cfinal2 = c1 + c2 + c3

    print(f"Your cards: [{c1}, {c2}], current score: {c1 + c2}")
    print(f"Computer's first card: {cc1}")
    while cfinal < 21 or cfinal2 < 21:
        next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if next_card == "y":
            print("\n")
            print(f"Your final hand: [{c1}, {c2}, {c3}], final score: {cfinal2}")
            print(f"Computer's final hand: [{cc1, cc2}], final score: {cc1 + cc2}")
        elif next_card == "n":
            print("\n")
            print(f"Your final hand: [{c1}, {c2}], final score: {cfinal}")
            print(f"Computer's final hand: [{cc1, cc2}], final score: {cc1 + cc2}")



elif play == "n":
    print("Goodbye!")
else:
    print("Invalid input!")



"""
    Your cards: [9, 10]
    Computer's first card:
    Type 'y' to get another card, type 'n' to pass: 
"""