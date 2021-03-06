"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after
 a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

"""

def move(up, down, left, right):
	vert = 0
	horiz = 0
	vert = vert + up - down
	horiz = horiz + left - right
	distance = (vert ** 2 + horiz ** 2) ** 0.5
	return round(distance)


print(move(5, 3, 3, 2))
print(move(1, 0, 1, 0))

"""
zero = 0, 0
start = 2, 3
first = 5, 6
distance0 = (2-0), (3-0)
distance1 = (5-2), (6-3)
"""
