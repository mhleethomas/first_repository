"""
File: extension4_narcissistic_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

SENTINEL = -100


def main():
    """
    1. print a welcome message
    2. get first input n from user
    3. check if it is equal SENTINEL
        if entering SENTINEL, end program
        if not entering SENTINEL, judge if it is a narcissistic number
    4. keep getting more n, and repeat step 3
    """

    print("Welcome to the narcissistic number checker!")
    n = int(input("n: "))
    constant_n = n
    # stores n in constant_n to be reassigned after n changes
    summation = 0
    power = 1

    if n == SENTINEL:
        # True scope: entering SENTINEL,end program
        print("Have a good one!")
    else:
        # False scope: judge if n is a narcissistic number
        while n >= 1:
            # while loop scope: get the amount of digits of n
            n = n // 10
            # remove the last digit from n and send back to while loop
            power += 1
            # count the digits with "power"
        power -= 1
        # "power" - 1 to solve OBOB
        n = constant_n
        # reassign the original value to n
        while n >= 1:
            # while loop scope: get every digit, and sum up according to narcissistic number rule
            digit = n % 10
            n = n // 10
            summation += digit ** power

        if summation == constant_n:
            # if statement scope: print judgment
            print(str(constant_n) + " is a narcissistic number")
        else:
            print(str(constant_n) + " is not a narcissistic number")

        while True:
            n = int(input("n: "))
            constant_n = n
            # stores n in constant_n to be reassigned after n changes
            summation = 0
            power = 1

            if n == SENTINEL:
                # True scope: entering SENTINEL,end program
                print("Have a good one!")
                break
            else:
                # False scope: judge if n is a narcissistic number
                while n >= 1:
                    # while loop scope: get the amount of digits of n
                    n = n // 10
                    # remove the last digit from n and send back to while loop
                    power += 1
                    # count the digits with "power"
                power -= 1
                # "power" - 1 to solve OBOB
                n = constant_n
                # reassign the original value to n
                while n >= 1:
                    # while loop scope: get every digit, and sum up according to narcissistic number rule
                    digit = n % 10
                    n = n // 10
                    summation += digit ** power

                if summation == constant_n:
                    # if statement scope: print judgment
                    print(str(constant_n) + " is a narcissistic number")
                else:
                    print(str(constant_n) + " is not a narcissistic number")


if __name__ == '__main__':
    main()
