# This program takes a string and converts it into a camelCase word/variable

# Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser".
# Optional extra question: print a warning message if the input will not produce a valid Python variable name. You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".
# Test your program, and comment your code.


sentence = input("Enter the sentence you would like to convert to camelCase: \n")
# Lists https://www.tutorialspoint.com/python/python_lists.htm
# Split https://www.tutorialspoint.com/python/string_split.htm
wordList = sentence.split(' ')
currentWord = 0
camelCaseSentence = ''
# Troubleshooting len with lists https://www.programiz.com/python-programming/methods/built-in/len
# String concatination https://waymoot.org/home/python_string/
# While loop to loop over each word in the wordList
while currentWord < len(wordList):
    # print(wordList[currentWord]) # Testing
    if currentWord != 0: # Make uppercase
        camelCaseSentence += (wordList[currentWord].capitalize())
    else: # Make lowercase http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
        camelCaseSentence += (wordList[currentWord].lower())
    currentWord += 1
# Prints the sentence in camelCase
print("Your sentence in camelCase: \n" + camelCaseSentence)
if camelCaseSentence.count('#') >= 1 or camelCaseSentence.count('+') >= 1 or camelCaseSentence.count('"') >= 1:
    print("This could not be a variable name because it contains a #, +, or \"")
else:
    print("This word does not contain: #, +, or \"")
# Simple way of checking if the camelCaseSentence starts with an integer
try:
    int(camelCaseSentence[0])
    print("This could not be a variable name because it starts with a number/integer")
# Catches the ValueError when trying to convert a variable into an integer without being an integer
except ValueError:
    print("The starting character is not a number.")

# For loop http://stackoverflow.com/questions/18294534/is-there-a-foreach-function-in-python3
# for word in wordList:

    # while letterPlace < len(sentence)
    #     letter = sentence[letterPlace]
    #     while letter != ' '
