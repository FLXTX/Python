
while True:
    phrase = input("Write something here: ")
    if phrase.isalpha():
        print(phrase.lower())
        break
    else:    
        print("Only words are allowed")
