

def puzzle1(secret_word, guess_limit):
    guess = ""
    guess_count = 0
    out_of_guesses = False

    while not(out_of_guesses) and guess.lower() != secret_word.lower():
        if guess_count < guess_limit:
            guess = input("Which animal has the longest neck? : ")
            guess_count += 1
            remaining_attempts = guess_limit - guess_count
            if guess.lower() != secret_word.lower():
                print("Wrong awnser. " + str(remaining_attempts) + " / " + str(guess_limit) + " attempts left")
        else:
            out_of_guesses = True    
    if out_of_guesses:
        print("Out of guesses.")
    else:    
        print("Correct!")



def puzzle2(secret_word, guess_limit):
    guess = ""
    guess_count = 0
    out_of_guesses = False

    while not(out_of_guesses) and guess.lower() != secret_word.lower():
        if guess_count < guess_limit:
            guess = input("Which animal was worshipped by ancient Egyptians? : ")
            guess_count += 1
            remaining_attempts = guess_limit - guess_count
            if guess.lower() != secret_word.lower():
                print("Wrong awnser. " + str(remaining_attempts) + " / " + str(guess_limit) + " attempts left")
        else:
            out_of_guesses = True    
    if out_of_guesses:
        print("Out of guesses.")
    else:    
        print("Correct!")



def puzzle3(secret_word, guess_limit):
    guess = ""
    guess_count = 0
    out_of_guesses = False

    while not(out_of_guesses) and guess.lower() != secret_word.lower():
        if guess_count < guess_limit:
            guess = input("Who is man's best friend? : ")
            guess_count += 1
            remaining_attempts = guess_limit - guess_count
            if guess.lower() != secret_word.lower():
                print("Wrong awnser. " + str(remaining_attempts) + " / " + str(guess_limit) + " attempts left")
        else:
            out_of_guesses = True    
    if out_of_guesses:
        print("Out of guesses.")
    else:    
        print("Correct!")


puzzle1("giraffe", 4)
print("Next question: ")
puzzle2("cat", 4)
print("Next question: ")
puzzle3("dog", 4)