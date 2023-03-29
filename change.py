print("Please enter an amount in cents less than a dollar")
money = int(input())
quarter = money//25
mod_quarter = money%25
dime = mod_quarter//10
mod_dime = mod_quarter%10
nickel = mod_dime//5
mod_nickel = mod_dime%5
penny = mod_nickel//1
print("Your change will be:")
print("Q:",quarter)
print("D:",dime)
print("N:",nickel)
print("P:",penny)