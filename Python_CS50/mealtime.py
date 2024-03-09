

def main():
    time_input = input("What time is it now?: ")
    hours = convert(time_input)
    if 7 <= hours < 8:
        print("It's breakfast time!")
    elif 12 <= hours < 13:
        print("It's lunch time!")
    elif 18 <= hours < 19:
        print("It's dinner time!")
    else:
        print("No food right now!")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    time_result =  hours + (minutes/60)
    return time_result

if __name__ == "__main__":
    main()