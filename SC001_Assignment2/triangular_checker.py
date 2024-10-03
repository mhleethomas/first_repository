"""
File: extension3_triangular_checker.py
Name:
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

SENTINEL = -100


def main():
    """
    1. print a welcome message
    2. get first input n from user
    3. check if it is equal SENTINEL
        if entering SENTINEL, end program
        if not entering SENTINEL, judge if n is a triangular number
    4. keep getting more n, and repeat step 3
    """

    print("Welcome to the triangular number checker!")
    n = int(input("n: "))
    summation = 0
    i = 1

    if n == SENTINEL:
        # True scope: entering SENTINEL,end program
        print("Have a good one!")
    else:
        # False scope: judge if n is a triangular number
        while n > summation:
            # while loop scope: sum up the positive integers until summation > n
            summation += i
            i += 1

        if n == summation:
            # if statement scope: print judgment
            print(str(n) + " is a triangular number")
        else:
            print(str(n) + " is not a triangular number")

        while True:
            # while loop scope: infinite loop
            n = int(input("n: "))
            summation = 0
            i = 1

            if n == SENTINEL:
                # True scope: entering SENTINEL,end program
                print("Have a good one!")
                break
            else:
                # False scope: judge if n is a triangular number
                while n > summation:
                    # while loop scope: sum up the positive integers until summation > n
                    summation += i
                    i += 1

                if n == summation:
                    # if statement scope: print judgment
                    print(str(n) + " is a triangular number")
                else:
                    print(str(n) + " is not a triangular number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
