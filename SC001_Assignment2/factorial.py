"""
File: extension1_factorial.py
Name: 李名翔 Thomas
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

SENTINEL = -100


def main():
	"""
	1. print a welcome message
	2. get first input n from user
	3. check if it is equal SENTINEL
		if entering SENTINEL, end program
		if not entering SENTINEL, calculate the factorial of n
	4. keep getting more n, and repeat step 3
	"""

	print("Welcome to stanCode factorial master!")
	n = int(input("Give me a number, and I will List the answer of factorial: "))
	multiplier = 1
	answer = 1

	if n == SENTINEL:
		# True scope: entering SENTINEL,end program
		print("- - - - - - See ya!-------------")
	else:
		# False scope: calculate the factorial of n
		while n >= multiplier:
			# while loop scope: multiply all the numbers less than n
			answer *= multiplier
			multiplier += 1

		print("Answer: " + str(answer))

		while True:
			# while loop scope: infinite loop
			n = int(input("Give me a number, and I will List the answer of factorial: "))
			multiplier = 1
			answer = 1

			if n == SENTINEL:
				# True scope: entering SENTINEL,end program
				print("- - - - - - See ya!-------------")
				break
			else:
				# False scope: calculate the factorial of n
				while n >= multiplier:
					# while loop scope: multiply all the numbers less than n
					answer *= multiplier
					multiplier += 1
				print("Answer: " + str(answer))


if __name__ == '__main__':
	main()
