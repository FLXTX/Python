
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))


# 2D lists

numer_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(numer_grid[0][0])     #Define the [row] and [column] to print


#Nested for loop

for row in numer_grid:      #Prints out all the rows
    print(row)

for row in numer_grid:      
    for col in row:
        print(col)