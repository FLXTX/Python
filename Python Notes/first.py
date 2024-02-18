from math import *


print ("Hello world")

print ("   /|")
print ("  / |")
print (" /  |")
print ("/___|")



character_name = "Felix"
character_age = 70
is_male = True
print ("There was a man named " + character_name + ",")
print ("He was " + str(character_age) + " years old")

character_name = "James"
character_age = 50
print ("He really liked the name " + character_name + ",")
print ("but he didn't like being " + str(character_age) + ".")

phrase = "Giraffe Academy"
print (phrase + " is cool!")

phrase = "Giraffe Academy"
print (phrase.upper().isupper())

print(len(phrase))  #phrase length

print (phrase[0])   #print selected character   
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))

print(2)
print(2.31231)
print(3 + 2.33)
print(3*(2+3))
print(10 % 3) # This is the modulus(mod) operator, prints out the remainder aka 10/3=3 with a ramainder of 1

my_num = 5
print(my_num)
print(str(my_num) + " is my favourite number")

my_num = -20
print(abs(my_num))      #give the absolute value of the int
print(pow(4, 6))      #to the power of
print(max(2, 4, 6, 8, 10))  #returns the biggest value
print(min(2, 4, 6, 8, 10))  #returns the smallest value
print(round(3.2))           #rounds the number

# these require the math library (from math import *)      
print(floor(10.7))  # gets the largest int thats <= to x
print(ceil(11.1))   # gets the largest int thats >= to x
print(sqrt(36))     # gets the square root of the int




