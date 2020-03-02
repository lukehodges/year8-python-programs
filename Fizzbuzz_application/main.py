import time
from year import years
def fizzbuzz():
	num = 0
	for i in range(100):
		num = num + 1
		num5 = num / 5
		num5 = str(num5)
		num3 = num / 3
		num3 = str(num3)
		if num3[-1] == '0':
			value = 'fizz'
		if num5[-1] == '0':
			value = "buzz"
		if num5[-1] != '0' and num3[-1] != '0':
			value = str(num)
		if num3[-1] == '0' and num5[-1] == '0':
			value = "fizzbuzz"
		print(value)
	for i in range(99):
		num = num - 1
		num5 = num / 5
		num5 = str(num5)
		num3 = num / 3
		num3 = str(num3)
		if num3[-1] == '0':
			value = 'fizz'
		if num5[-1] == '0':
			value = "buzz"
		if num5[-1] != '0' and num3[-1] != '0':
			value = str(num)
		if num3[-1] == '0' and num5[-1] == '0':
			value = "fizzbuzz"
		print(value)
fizzbuzz()
years.leap_year()
years.guess()

