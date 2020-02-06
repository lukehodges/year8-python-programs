#list of all of the users
users = [
	{'name': 'luke', 'pass': 20},
	{'name': 'meme', 'pass': 50},
	{'name': 'lelo', 'pass': 20},
	{'name': 'hundred', 'pass': 20},
	{'name': 'sam', 'pass': 20},
	{'name': 'static', 'pass': 20}
	]

username = input("enter username")
# enters the users name
username1 = username[0]#grabs the first and second characters of the string
username2 = username[1]
possible = [user['name'] for user in users if user['name'][0] == username1 if user['name'][1] == username2]
#compare the varaibles to the string
print(possible)
#print the possible results
