# importing math for square routing (line 24)
import math
#making nececary variables
radius = 2
pi = 3.14159265358979
height = 3
line = height

def sphere(radius, pi):
	#volume = 3/4 pi * radius to the power of 3
	pi2 = pi/4 *3 #3/4 of pi
	radius = radius*radius*radius # cubing the radius
	volume = pi2*radius 
	print(volume)
	volume = 0

def cone(radius, height, pi):
	#volume = height/3 * pi * radius squared
	height = height/3
	radius = radius*radius
	volume = pi*radius*height
	print(volume)

def cylinder(radius, height, pi):
	# volume = pi * radius squared * heightt
	volume = pi*radius*radius*height
	print(volume)
	
def d20(line):
	#volume = 5(3+squrt(5)) / 12 * line cubed
	#line is the length of one of the sides
	volume = math.sqrt(5)
	volume = volume + 3
	volume = volume*5
	volume = volume/12
	line = line*line*line
	volume = volume*line
	print(volume)

#remove hash to run
#cylinder(radius, height, pi)
#d20(line)
#sphere(radius, pi)
