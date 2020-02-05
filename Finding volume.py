import math
radius = 2
pi = 3.14159265358979
height = 3
line = height
def sphere(radius, pi):
	pi2 = pi/4 *3
	radius = radius*radius*radius
	volume = pi2*radius
	print(volume)
	volume = 0

def cone(radius, height, pi):
	height = height/3
	radius = radius*radius
	volume = pi*radius*height
	print(volume)

def cylinder(radius, height, pi):
	volume = pi*radius*radius*height
	print(volume)
def d20(line):
	volume = math.sqrt(5)
	volume = volume + 3
	volume = volume*5
	volume = volume/12
	line = line*line*line
	volume = volume*line
	print(volume)

#cylinder(radius, height, pi)
d20(line)
#sphere(radius, pi)
