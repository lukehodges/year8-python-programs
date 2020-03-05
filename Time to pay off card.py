### 04/03/2020
### Luke Hodges
### Debt calculator

# start up message
print("---------------------")
print("   debt calculator   ")
print("---------------------")

# getting the information on the card
print("\n enter the interest rate")
interest = input("> ")
interest = int(interest)
print("\n enter the amount on the card")
price = input("> ")
price = int(price)
print("\n enter the amount you are willing to save for the card")
save = input("> ")
save = int(save)

# finding the total price of the card
totalprice = price / interest
totalprice = price + totalprice
print(totalprice)

# calculating the time to pay off the card
time = totalprice / save
time = str(time)
print(time + " months to pay off your card")
