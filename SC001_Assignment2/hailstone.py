"""
File: hailstone.py
Name: 李名翔 Thomas
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    1. print a welcome message
    2. get n from user
    3. judge if n is an odd number or a even number
        if n is an odd number, make it 3 * n +1
        if n is an even number, make it n/2
    3. repeat step 3 until n is equal to 1
    4. print how many times the program took to make n equals to  1
    """

    print("This program computes Hailstone sequences.")
    print()
    n = int(input("Enter a number: "))
    # get a positive integer n from user
    step = 0
    # ste a counter to count how many times the program will take

    while n != 1:
        # while loop scope: calculate Hailstone sequence until n == 1
        if n % 2 == 1:
            # True scope: n is odd
            m = 3 * n + 1
            print(str(n) + " is odd, so I make 3n+1: " + str(m))
        else:
            # False scope: n is even
            m = n // 2
            print(str(n) + " is even, so I take half: " + str(m))
        n = m
        # reassign value m to variable n
        step += 1
        # count the steps the program took

    print("It took " + str(step) + " steps to reach 1")


if __name__ == "__main__":
    main()
