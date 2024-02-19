

def main():
    question = input("What is the Awnser to the Great Question on Life, the Universe and Everything? ")
    if question == "42" or question.lower() == "forty-two" or question.lower() == "forty two":
        print("Yes")
    else:
        print("No")


main()