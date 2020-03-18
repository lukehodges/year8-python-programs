import random
ticketshas = []
for i in range(50):
	ticket = random.randint(1,random.randint(1,100))
	if ticket not in ticketshas:
	  ticketshas.insert(0,ticket)
print(ticketshas)
not_in_box = True
while not_in_box:
	guess = input("enter your loto number\n> ")
	guess = int(guess)
	if guess in ticketshas:
		print("number already selected")
	else:
		print("number is now in the box")
		ticketshas.insert(0,guess)
		not_in_box = False
winner = str(random.choice(ticketshas))
print("-------------------")
print("--- the lottery ---")
print("-------------------\n")
print("\n the results are in...")
print("the winner is number " + winner)
winner = int(winner)
if guess == winner:
	print("you won!")
else:
	print("you did not win")
