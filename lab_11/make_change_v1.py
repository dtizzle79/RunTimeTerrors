# make_change version 1
coin_value = {'pennies': 1,
              'dimes': 10,
              'nickels': 5,
              'quarters': 25
              }

total_amount = input("Enter dollar amount 0.00 \n>")
total_amount = float(total_amount)
total_amount = total_amount * 100
number_of_quarters = (total_amount // coin_value['quarters'])
number_of_pennies_left = (total_amount % coin_value['quarters'])
number_of_dimes_left = (number_of_pennies_left // coin_value['dimes'])
number_of_nickels_left = (number_of_dimes_left // coin_value['nickels'])
print(f"You have {number_of_quarters} quarters {number_of_pennies_left} pennies {number_of_dimes_left} dimes and {number_of_nickels_left} nickels.")
