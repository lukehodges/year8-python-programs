import random
number = random.randint(1,100)
print("the number to guess: ",number)
def midway(low,high):
	one = low + high
	return int(one /2)
low = 0
high = 100
guess = 0
while 1:
	guess += 1
	print("the computer makes a guess",midway(low,high))
	if midway(low,high) > number: high = midway(low,high)
	elif midway(low,high) < number: low = midway(low,high)
	else:
		break
print("the computer found the number")
print("number of guesses: ",guess)
