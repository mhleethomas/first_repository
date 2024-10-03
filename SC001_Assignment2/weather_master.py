"""
File: weather_master.py
Name: 李名翔 Thomas
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
SENTINEL = -100


def main():
	"""
	1. print a welcome message
	2. get first input n from user
	3. check if it is equal SENTINEL,
		if entering SENTINEL, end program
		if not entering SENTINEL, print the results, including:
			highest temperature
			lowest temperature
			average
			how many cold days
	"""
	print('stanCode "Weather Master 4.0"!')

	data = int(input("Next temperature: (or " + str(SENTINEL) + " to quit)? "))
	# get first input n from user
	maximum = data
	minimum = data
	summation = 0
	amount_of_data = 1
	cold_days = 0

	if data == SENTINEL:
		# True scope: entering SENTINEL,end program
		print("No temperatures were entered.")
	else:
		# False scope: first data is NOT the SENTINEL
		summation += data
		# calculate summation
		if data < 16:
			# True scope: count of cold days +1
			cold_days += 1

		while True:
			# while loop scope: an infinite loop
			data = int(input("Next temperature: (or " + str(SENTINEL) + " to quit)? "))

			if data == SENTINEL:
				# True scope: entering SENTINEL,end program
				break
			elif data > maximum:
				# True scope: assign data to maximum
				maximum = data
				summation += data
			elif data < minimum:
				# True scope: assign data to minimum
				minimum = data
				summation += data
			else:
				# False scope: data is between minimum and maximum
				summation += data
			amount_of_data += 1

			if data < 16:
				# True scope: count of cold days +1
				cold_days += 1

		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		average = summation / amount_of_data
		print("Average = " + str(average))
		print(str(cold_days) + " cold day(s)")


if __name__ == "__main__":
	main()
