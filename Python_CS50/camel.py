# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding 
# name in snake case. Assume that the user’s input will indeed be in camel case.


def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case


def main():
    camel_case = input("camelCase phrase:")
    snake_case = camel_to_snake(camel_case)
    print("snake_case:", snake_case)

if __name__ == "__main__":
    main()

