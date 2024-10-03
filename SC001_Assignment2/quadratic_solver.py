"""
File: quadratic_solver.py
Name: 李名翔 Thomas
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	1. print a welcome message
	2. ask the user to input a, b, c for the equation: ax^2 + bx + c = 0
	3. compute b * b - 4ac as discriminant
	4. judge the discriminant
		if discriminant > 0, then solve and print 2 real roots
		else if discriminant = 0, then solve and print 1 real root
		else, print 'no real roots'
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	discriminant = b*b - 4 * a * c
	# calculate the discriminant for further if statement usage

	if discriminant > 0:
		# True scope: discriminant is greater than 0
		# print the two real roots
		root1 = (-1 * b + math.sqrt(discriminant)) / (2 * a)
		root2 = (-1 * b - math.sqrt(discriminant)) / (2 * a)
		print("Two roots: " + str(root1) + "," + str(root2))
	elif discriminant == 0:
		# True scope: discriminant is equal to 0
		# print the one real root
		root1 = (-1 * b + math.sqrt(discriminant)) / (2 * a)
		print("One root: " + str(root1))
	else:
		# False scope: discriminant is less than 0
		# print "No real roots"
		print("No real roots")


if __name__ == "__main__":
	main()
