import random
class years():
	def leap_year():
		print('enter the year you want to test')
		inp = input('> ')
		inp = int(inp)
		inp4 = inp / 4
		inp4 = str(inp4)
		if inp4[-1] == '0':
			print('leapyear')
	def guess():
		lists = []
		guesses = 0
		num = random.randint(1,1000)
		print("guess my number")
		wright = False
		while wright == False:
			inp = input('> ')
			inp = int(inp)
			if inp in lists:
				print("guess already made")
			if inp not in lists:
				if inp > num:
					lists.append(inp)
					print("lower")
					guesses = guesses + 1
				elif inp < num:
					print("higher")
					lists.append(inp)
					guesses = guesses + 1
				elif inp == num:
					num = str(num)
					print("correct, my number was " + num)
					guesses = str(guesses)
					print("you guessed my number after " + guesses + " guesses")
					print(lists)
					wright = True
