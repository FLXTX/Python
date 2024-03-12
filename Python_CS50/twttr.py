


def twttr(phrase):
    phrase = ""
    
    for letter in phrase:
        if letter in "AEIOUaeiou":
            phrase = phrase + ""
    return phrase

print(twttr(input("Enter your phrase: ")))

