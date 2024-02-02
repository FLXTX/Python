


is_male = True

if is_male:
    print("Hey dude!")
else:
    print("Hey girl!")


is_male = False
is_tall = True

if is_male and is_tall:
    print("Hey dude, you are tall!")
elif is_male and not(is_tall):
    print("Hey dude, you are short!") 
elif not(is_male) and is_tall:
    print("Hey girl, you are tall!")         
else:
    print("Hey girl, you're not tall!")    


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(2, 3, 4))    


i = 1
while i <= 10:
    print(i)
    i += 1      #Adds 1 to i
print("Done with loop") 