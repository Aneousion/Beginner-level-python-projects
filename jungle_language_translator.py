print("""

Welcome to the Jungle Language Translator
From github.com/aneousion

""")

sentence = input("Input the sentence: ").lower()  # lower() changes the sentence to lower case

translated = ""  # empty variable to store the translated letters

vowels = [" ", "a", "e", "i", "o", "u"]  # list of vowels in alphabetical order, position 0 is empty

for letter in sentence:
    if letter == "a":                               # if the letter is "a"
        continue                                    # skip it
    elif letter in ["0", "1", "2", "3", "4", "5"]:  # if the letter is a number
        translated += vowels[int(letter)]           # and the vowel that is at that position to the translated variable
    else:                                         # if the letter is not "a" or a number e.g special chars like !, space, >,@,etc
        translated += letter                      # simply add it to the translated variable

print(f"\nYour decoded message is: \n{translated.title()}")
