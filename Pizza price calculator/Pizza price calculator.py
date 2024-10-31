
pizza_prices = {
    "S": 200,   
    "M": 500,  
    "L": 1200   
}


pepperoni_prices = {
    "S": 90,   
    "M": 130,   
    "L": 180  
}
extra_cheese_price = 50 
coke_price = 40

print("Welcome to the Pizza Price Calculator!")

size = input("Choose your pizza size (S for Small, M for Medium, L for Large): ").upper()

if size not in pizza_prices:
    print("Invalid size entered! Please choose S, M, or L.")
else:
    total_price = pizza_prices[size]

   
    add_pepperoni = input("Do you want to add pepperoni? (yes/no): ").lower()
    if add_pepperoni == "yes":
        total_price += pepperoni_prices[size]

    add_extra_cheese = input("Do you want to add extra cheese? (yes/no): ").lower()
    if add_extra_cheese == "yes":
        total_price += extra_cheese_price

    add_coke = input("Would you like to add a Coke? (yes/no): ").lower()
    if add_coke == "yes":
        total_price += coke_price

    print(f"\nYour final bill is: Rs {total_price:.2f}/- only")
