'''In a file called faces.py, implement a function called convert that accepts a str as input and returns 
that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) 
and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, 
and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own 
as an argument to input. Be sure to call main at the bottom of your file.'''

def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase

def main():
    user_input = input("Write some emojis on your keyboard: ")
    new_text = convert(user_input)
    print(new_text)


main()