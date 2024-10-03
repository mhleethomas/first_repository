"""
File: prime_checker.py
Name: 李名翔 Thomas
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

SENTINEL = -100


def main():
	"""
	1. print a welcome message
	2. get first input n from user
	3. check if it is equal SENTINEL
		if entering SENTINEL, end program
		if not entering SENTINEL, check if n is a prime number
	4. keep getting more n, and repeat step 3
	"""

	print("Welcome to the prime checker")
	n = int(input("n: "))
	factor = 1
	factor_count = 0

	if n == SENTINEL:
		# True scope: entering SENTINEL,end program
		print("Have a good day")
	else:
		# False scope: check if n is a prime number

		while factor <= n:
			# while loop scope: find all factors of n
			if n % factor == 0:
				# True scope: is a factor of n
				factor_count += 1
				factor += 1
			else:
				# False scope: is not a factor of n
				factor += 1

		if factor_count == 2:
			# True scope: found only 2 factors (1 and itself)
			print(str(n) + " is a prime number")
		else:
			# False scope: found more than 2 factors (or less than, but will not happen)
			print(str(n) + " is not a prime number")

		while True:
			# while loop scope: an infinite loop
			n = int(input("n: "))
			factor = 1
			factor_count = 0

			if n == SENTINEL:
				# True scope: entering SENTINEL,end program
				print("Have a good day")
				break
			else:
				# False scope: check if it is a prime number
				while factor <= n:
					# while loop scope: find all factors of n
					if n % factor == 0:
						# True scope: factor is a factor of n
						factor_count += 1
						factor += 1
					else:
						# False scope: is not a factor of n
						factor += 1
				if factor_count == 2:
					# True scope: found only 2 factors (1 and itself)
					print(str(n) + " is a prime number.")
				else:
					# False scope: found more than 2 factors (or less than, but will not happen)
					print(str(n) + " is not a prime number.")


if __name__ == "__main__":
	main()
