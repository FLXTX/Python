


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Jim", "Kevin", "Michael", "Jim", "Dwight", "Pam", "Jim", "Angela"]



'''
print(friends[1])
print(friends[-1])
print(friends[1:])  #prints from index 1 forward
print(friends[1:4]) #prints from index 1 until 4 but not including


friends[1] = "Andy"     #change list entries
print(friends[1])

'''

friends2 = friends.copy()
print(friends2)

friends.extend(lucky_numbers)   #adds to list
print(friends)

friends.append("Creed")     # append adds to the end of the list
print(friends)

friends.insert(1, "Kelly")  # insert requires 2 inputs, which position and what to add
print(friends)

friends.sort()      # sorts the list in ascending order, cannot sort mixed list of int and str
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

friends.remove("Pam")
print(friends)

friends.pop()       #pop removes the last element on the list
print(friends)

print(friends.index("Dwight"))      # gives the index of selected name
# print(friends.index("Mike"))        # if something is not on the list it will give an error


print(friends.count("Jim"))         # counts how many are on the list

friends.clear()     # removes everything from the list
print(friends)

#Tuple is a structure I can store multiple pieces of information, similar to lists
#Tuple can't be changed or modified unlike lists
# Tuple is used with data that is never going to change

coordinates = (4, 5)
print(coordinates[0])

coordinates = [(4, 5), (6, 7), (80, 90)]    # You can also make a list of tuples