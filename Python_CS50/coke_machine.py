

def main():
    
    coke_cost = 50
    initial_coins = 0
    coins_inserted = initial_coins
    while coins_inserted < coke_cost:
        user_input = int(input("Insert coins (5c)(10c)(20c): "))
        if user_input == 5 or user_input == 10 or user_input == 25:
            coins_inserted += user_input
            print("Coins inserted: " + str(coins_inserted) + "/" + str(coke_cost))
        else:
            print("Not correct currency")
            print("Coins inserted: " + str(coins_inserted) + "/" + str(coke_cost))
    if coins_inserted > coke_cost:
        overpaid_amount = coins_inserted - coke_cost
        print("You gave to much, here is " + str(overpaid_amount) + " coins back." )
    print("That's 50 coins, here's your coke !")

main()