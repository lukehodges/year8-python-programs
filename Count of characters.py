### 04/03/2020
### Luke Hodges
### count of character finder

# making the string
string = "hello world"
data = []

# converting the string to a list
for d in string:
	data.append(d)
print(data)

# sorting the list into order
data.sort(reverse = False)
print(data)

# printing out the letter and the number of appearances it has
for d in data:
	d1 = data.count(d)
	print(d, d1)
