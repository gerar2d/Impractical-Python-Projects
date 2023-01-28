"""Turn a word into its Pig Latin equivalent."""
import sys

VOWELS = 'aeiouy'

while True:
    word = input("Type a word and get its pig Latin translation: ")

    if word[0] in VOWELS:
        pig_Latin = word + 'way'
    else:
        pig_Latin = word[1:] + word[0] + 'ay'  #[1:] start from position one + [0] add position 0 + ay  ex. hello = ello+h+ay.
    print()
    print(f"{pig_Latin}")
    
    try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
    if try_again.lower() == "n":
        sys.exit()