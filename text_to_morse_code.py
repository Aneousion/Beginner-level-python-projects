alphabets = {
    "A": ".--",
    "B": "-..",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.--",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/"
}
morses = {value: key for key, value in alphabets.items()}


def txt_to_morse(text):
    morse = ""
    for letter in text.upper():
        morse += alphabets[letter] + " "
    return morse


def morse_to_text(morse):
    text = ""
    for letter in morse.split(" "):
        text += morses[letter]
    return text

while True:
    response = input("Type 'ttm' for text to morse code, 'mtt' for morse to text and 'q' to quit:\n")
    if response.lower() == "ttm":
        print(txt_to_morse(input("Text: ")))
    elif response.lower() == "mtt":    
        print(morse_to_text(input("morse: ")))
    else:
        break 
