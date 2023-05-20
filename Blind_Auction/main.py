import os
import art
print(art.logo)

place_holder = "NA"
person = {}

another_person = True
while another_person:
    name = input("Enter your name: ")
    bid_price = int(input("Enter bid price: "))

    person[name] = bid_price

    result = input("Are there other bidders?").lower()
    if result == "no":
        another_person = False
        max_value = max(person.values())
        max_key = max(person, key = person.get)
        print(f"The highest bidder is {max_key} with ${max_value} ")
    elif result == "yes":
        os.system("cls")