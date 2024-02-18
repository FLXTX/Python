

def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase

def main():
    user_input = input("Write some emojis on your keyboard: ")
    new_text = convert(user_input)
    print(new_text)


main()