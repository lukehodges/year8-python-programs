stringinp = str(input("enter the string\n> "))
array = []
for i in range(0,len(stringinp)):
	print(stringinp[i])
	array.insert(0,stringinp[i])
print(array)
array = []
print("\n\n\n")
for i in range(len(stringinp),0,-1):
	print(i)
	array.insert(0,stringinp[i-1])
print(array)
