# star athelete
# Luke Hodges
# 27/03/2020
lst = [] # create a list for the track times
laps = int(input("enter the number of laps the teacher must run\n> "))
for i in range(laps): # reapeat for number of tracks run
	lst.append(float(input("enter the laptime in seconds")))
print("the teacher runs",laps,"laps")
print("the teacher's fastest lap was ",min(lst)," seconds")# fastest time(smallest number)
print("the teacher's slowest lap was ",max(lst))# slowest time(largest number)
print("the average lap time was",sum(lst)/len(lst))# average total time/ laps
