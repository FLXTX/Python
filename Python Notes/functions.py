




# def keyword is required to use functions

def say_hi() :          # all the code coming after this line is in the function and it HAS TO BE INDENTED!!
    print("hello user")
                               

print("top")
say_hi()                        # to access the function I have to call it
print("bottom") 

def say_hi(name, age) :          # A parameter is a piece of info I give to the function
    print("Hello " + name + ", you are " + age + " old.")

say_hi("Mike", "35")  
say_hi("Steve", "55")            

def cube(num):          # return keyword returns information from a function and breaks out of the function
    return num*num*num  

print(cube(3))

def cube(num):          
    return num*num*num  

result = cube(4)
print(result)