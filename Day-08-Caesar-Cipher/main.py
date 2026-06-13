# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caeser(text,shift,direction):
    display = ""
    if direction == "decode":
        shift *= (-1)
    for letter in text:
        if letter not in alphabet:
            display += letter
        else:

            idx = alphabet.index(letter) + shift
            idx_main = idx % len(alphabet)
            letter = alphabet[idx_main]
            display += letter
    print(f"Your {direction}d result: {display}")
    choice = input("Type 'Yes' if you want to go again.Otherwise type 'No'\n").lower()
    if choice == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caeser(text,shift,direction)
    else:
        return

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caeser(text,shift,direction)

