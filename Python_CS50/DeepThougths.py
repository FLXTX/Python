# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
# Otherwise output No.

Hints

def main():
    question = input("What is the Awnser to the Great Question on Life, the Universe and Everything? ")
    if question == "42" or question.lower() == "forty-two" or question.lower() == "forty two":
        print("Yes")
    else:
        print("No")


main()