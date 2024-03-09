

def calculator(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y =="/":
        return x / z
    
def main():
    expression = input("Let's start calculating: ")
    x,y,z = expression.split(" ")
    x = float(x)
    z = float(z)
    result = calculator(x, y, z)
    print(result)

main()