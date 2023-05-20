import os
import art
print(art.logo)

place_holder = "NA"

another_person = True
while another_person:
    name = input("Enter your name: ")
    bid_price = int(input("Enter bid price: "))

    person = {name: bid_price}

    result = input("Are there other bidders?").lower()
    if result == "no":
        another_person = False
        print(f"The highest bidder is: {place_holder} with ${place_holder} ")
    elif result == "yes":
        os.system("cls")
