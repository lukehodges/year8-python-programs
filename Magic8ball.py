from random import randint
results = ["It is certian","It is decidedly so","Without a doubt","yes-definitely","you may rely on it","As i see it,yes","Most likely","Outlook good","yes","Signs point to yes","Reply hazy, try agin","ask again later","Better not tell you now","cannot predict now","concentrate and ask again","dont count on it","my reply is no","Outlook not so good","very doubtful"]
print(len(results))
while 1:
	wish = input("enter your wish\n> ")
	spin = randint(0,19)
	spin -= 1
	print("you spin the eight ball...\n> ", results[spin])
