# Beginner-level-python-projects
Actively growing list of beginner-level python projects.


# 1.	 BMI Calculator
This program calculates your Body Mass Index (BMI) using your weight and height. Your BMI is your weight, in kilograms, divided by two times your height, in meters. (kg/m)
BMI 18 and below – Underweight
BMI 18 to 25 – Normal weight
BMI 25 to 30 – Overweight
BMI 30 to 35 – Obese
BMI 35 and above – Clinically obese
Write a python program that takes weight, in kg, and height, in meters, and outputs your BMI and the corresponding weight status. 

Example:

```
What is your height in m?: 
1.8
What is your weight in kg?: 
70
Your BMI is 22, you have a normal weight

Process finished with exit code 0 
```

[solution](Bmicalculator.py)

# 2.	Factor Finder
This program finds the factors of a given number.
Write a python program that takes a number and outputs the factors of the number.
Example:

```
Enter the number to be checked: 
150
factors of 150 are 1,2,3,5,6,10,15,25,30,50,75,150.

Process finished with exit code 0 
```

[solution](factor_finder.py)

# 3.	Jungle Language Translator
Where I’m from there is a language called jungle language which is simply tweaked English Language.
Vowels: a e I o u
Jungle vowels: 1 2 3 4 5
Jungle consonants have the letter “a” at the end of each letter. E.g. b is ba, g is ga, k is ka, etc
Write a python program to translate jungle language to English Language.
Example:

```
Input the sentence: 
Ba215taya 3sa ta2rara4ra
Your decoded message is: 
Beauty Is Terror

Process finished with exit code 0.
```

[solution](jungle_language_translator.py)

# 4.	Leap Year Calculator
This program takes a year and outputs “it’s a leap year” if it’s a leap year and otherwise if its not.
A year is a leap year if it is evenly divided by 4 and it’s not evenly divided by 100.
A year is a leap year if it is evenly divided by 4, evenly divided by 100 and evenly divided by 400.
Hint: (1) Use the modulo (%)
(2) it is not a leap year if it is evenly divided 4 and evenly divided 100

Example:

```
Which year would you like to check? 
1916

This is a leap year
Process finished with exit code 0.
```

[solution](leap_year_calculator.py)

# 5.	Fibonacci
The Fibonacci Sequence is based on the following formula:
f(n) = 0, if n = 0 
f(n) = 1, if n=1
 f(n) = f(n-1 )+ f(n-2), if n>1
Write a program to calculate the value of f(n) with a given n input by console.
Example:
``` 
input n:
7
output:
13
Process finished with exit code 0.
```
Hint: Define a recursive function

[solution](fibonacci.py)

# 6. Text To Morse Code Converter
A program that converts plain text to morse code and vice versa.
Read this [article](https://en.wikipedia.org/wiki/Morse_code) on morse codes and write a program that converts plain text to morse code and morse codes to plain text.
Example:
 ```
Type 'ttm' for text to morse code, 'mtt' for morse to text and 'q' to quit:
ttm
Text: hello world 123
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. / .---- ..--- ...-- 
Type 'ttm' for text to morse code, 'mtt' for morse to text and 'q' to quit:
mtt
morse: .... . .-.. .-.. --- / .-- --- .-. .-.. -.. / .---- ..--- ...--
HELLO WORLD 123
Type 'ttm' for text to morse code, 'mtt' for morse to text and 'q' to quit:
q

Process finished with exit code 0

```
Hint: Define a function for text to morse and another for morse to text.

[solution](text_to_morse_code.py)
