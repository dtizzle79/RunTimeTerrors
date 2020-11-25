# make change version 2
coin_value = [('half-dollar', 50),('quarter', 25),('dime', 10),('nickel', 5),('penny', 1)]

total_amount = input("Enter dollar amount 0.00 \n> ")
total_amount = float(total_amount)
total_amount = total_amount * 100
half_dollars = (total_amount // coin_value[0][1])
quarters = (total_amount % coin_value[0][1] // coin_value[1][1])
pennies = (coin_value[2][1] // coin_value[4][1])
dimes = (pennies // coin_value[2][1])

print(f"{half_dollars}, {quarters}, {dimes} , {pennies}") 
