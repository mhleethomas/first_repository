"""
File: extension2_number_checker.py
Name: 李名翔 Thomas
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

SENTINEL = -100


def main():
    """
    1. print a welcome message
    2. get first input n from user
    3. check if it is equal SENTINEL
        if entering SENTINEL, end program
        if not entering SENTINEL, judge if n is a "perfect number" or "abundant number" or "deficient number"
    4. keep getting more n, and repeat step 3
    """

    print("Welcome to the number checker! ")
    n = int(input("n: "))
    factor = 1
    factor_counts = 0
    factor_summation = 0

    if n == SENTINEL:
        # True scope: entering SENTINEL,end program
        print("Have a good one!")
    else:
        # False scope: judge n
        while n > factor:
            # while loop scope: find all factors of n (except n)
            if n % factor == 0:
                # True scope: is a factor of n
                factor_summation += factor
                factor += 1
                factor_counts += 1
            else:
                # True scope: is NOT a factor of n
                factor += 1

        if factor_summation == n:
            # if statement scope: print judgment
            print(str(n) + " is a perfect number")
        elif factor_summation > n:
            print(str(n) + " is a abundant number")
        else:
            print(str(n) + " is a deficient number")

        while True:
            # while loop scope: infinite loop
            n = int(input("n: "))
            factor = 1
            factor_counts = 0
            factor_summation = 0

            if n == SENTINEL:
                # True scope: entering SENTINEL,end program
                print("Have a good one!")
                break
            else:
                # False scope: judge n
                while n > factor:
                    if n % factor == 0:
                        # True scope: is a factor of n
                        factor_summation += factor
                        factor += 1
                        factor_counts += 1
                    else:
                        # True scope: is NOT a factor of n
                        factor += 1

                if factor_summation == n:
                    # if statement scope: print judgment
                    print(str(n) + " is a perfect number")
                elif factor_summation > n:
                    print(str(n) + " is a abundant number")
                else:
                    print(str(n) + " is a deficient number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
