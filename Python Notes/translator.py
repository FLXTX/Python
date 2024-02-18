def translate(phrase):
    translation = ""
    for letter in phrase:                               #Replaces every letter in array with specified letter
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
    
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))        