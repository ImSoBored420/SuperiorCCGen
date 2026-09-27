import json
import random as r

"""

The few corners cut here were: fudging it on the expiration date to make it always applicable,
and making the cards always Luhn valid, since some companies do not apply to the Luhn algorithm's ubiquity

"""

#open json
with open("card_brands.json", "r") as file:
    file_contents = file.read()
    card_brands: dict = json.loads(file_contents)

#lowkey useless
def main():
    try:
        menu()
        
    except KeyboardInterrupt:
        print("Ctrl + C pressed! Exiting...")

#self
def menu():
    choice = input("Input brand: ").lower()

    if not card_brands.get(choice):
        print(f"Card type not found: {choice}")

    length = setLength(choice)
    prefix = setPrefix(choice)

    print(f"Card number: {returnNumber(length, prefix)}\nCVV:{r.randint(000,999)}\nEXP: {r.randint(1,12)}/{r.randint(1,29)}")

#abstractions of various tasks
def selectionOutput(choice):
    print(f"{choice} selected. \nApplying... ")

def setLength(choice) -> dict: # for future note, this returns a specific type in a function instead of warranting later specification ->
    return card_brands[f"{choice}"]["card_rules"][0]["card_lengths"]

def setPrefix(choice) -> dict:
    return card_brands[f"{choice}"]["card_rules"][0]["card_prefixs"]

def luhn(number):
    checksum = 0

    for i, digit in enumerate(reversed(number)):
        digit = int(digit)

        if i % 2 == 1:
            digit *= 2

            if digit > 9:
                digit -= 9

        checksum += digit

    return checksum % 10 == 0


def returnNumber(length, prefix):
    length = r.choice(length)
    prefix = r.choice(prefix)

    number = prefix + ''.join(
        r.choices("0123456789", k=length - len(prefix) - 1)
    )

    for check_digit in range(10):
        candidate = number + str(check_digit)

        if luhn(candidate):
            return candidate
        
#no module 
if __name__ == "__main__":
    main()