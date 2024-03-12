


def twttr(phrase):
    new_phrase = ""
    
    for letter in phrase:
        if letter not in "AEIOUaeiou":
            new_phrase += letter
    return new_phrase

print(twttr(input("Enter your phrase: ")))

'''
def twttr(phrase):
    new_phrase = ""
    
    for letter in phrase:
        if letter not in "AEIOUaeiou":
            new_phrase += letter
    
    return new_phrase

print(twttr(input("Enter your phrase: ")))
'''