# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.


def main():
    mass = int(input("Enter mass in kilograms: "))
    lightspeed = 300000000
    energy = mass * lightspeed ** 2
    print("The awnser is " + str(energy) + " joules")
    return energy

main()

