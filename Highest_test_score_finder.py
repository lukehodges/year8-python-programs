### 02/03/2020
### Luke Hodges
### Highest Test Scorer Finder

# storing the test scores in a dictionary
results = {
	"luke":120,
	"ben":40,
	"john": 100,
	"mary": 76,
	"elizabeth": 92,
	"teacher": 130
}

# making a list to organise the test scores
result = []

# collecting the information from the dictionary
for k in results:

	# collecting the persons score
	v = results[k]

	# converting score from int to str
	v = str(v)
	final = k + " got " + v

	# adding result to list
	result.append(final)

# sorting the list from highest to lowest
result.sort(reverse = True)

# printing results out
print(result)
for i in result:
	print(i)
