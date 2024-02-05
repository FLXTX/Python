
'''
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun : ")
celebrity = input("Enter a celebrity name: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''

name = input(" Who goes there?")
print("Well hello " + name + ". Let's play a game!! ")
print("OK. First I have to get to know you a bit....")
gender = input("Are you  a man or a woman? ").lower()

if gender == "man":
    title = "Sir"
else:
    title = "Lady"
print("Oh brave hero " + title + " " + name + ", ")    
dr_adjective = input(" How do you like your dragons? ").upper()
pi_noun = input("And what kind of pizza do you like? ").upper()
hat_noun = input("Okay, name a material: ").upper()
color = input("And what is your favourite colur? ").upper()
liquid = input("And favourite drink? ").upper()
magic_noun = input("Good, good... Now give me an object: ").upper()
animal = input("What is your favourite animal? ").upper()
socks = input(" Now give me a random adjective: ").upper()
emotion = input("What emotion describes you the best? ").upper()
print()
print("In a land of " + (dr_adjective) + " dragons and " + pi_noun + " pizza,")
print()
print("A strange hero named " + title + " "+ name + " sang opera.")
print()
print("While wearing a hat made of " + hat_noun + " on his head.")
print()
print("He danced with a " + color + " penguin, 'til they both fell into " + liquid + ".")
print()
print("The quest for the magical " + magic_noun + " was quite absurd,")
print()
print("With a sidekick " + animal + " who only spoke in rhyming words.")
print()
print("They encountered a wizard with an addiction for " + socks + " socks,")
print()
print("And the tale ended with laughter and " + emotion + " on the docks!")
print()
print("There you go " + title + " " + name + ", that was quite the adventure") 
print()
input("Press ENTER to exit ...")
