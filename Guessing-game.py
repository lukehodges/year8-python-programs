# Guessing Game
# Luke Hodges
# 27/03/2020
import random
num = int(input("input your number\n> "))
	
guess = random.randint(1,1000)
temp = 1000
bottom = 1
times = 0
while guess != num:
	times += 1
	guess = random.randint(bottom,temp)
	if guess > num:
		temp = guess
	if guess < num:
		bottom = guess
	print("the computer guesses",guess)
print("the computer guessed correct",num,"!")
print("number of guesses: ",times)
