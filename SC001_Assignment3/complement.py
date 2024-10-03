"""
File: complement.py
Name: 李名翔 Thomas
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    print the return value of the "build_complement" function
    if the given DNA string is empty, it will show a error message
    else print the corresponding DNA pair
    """
    print(build_complement('ATC'))  # TAG
    print(build_complement(''))  # DNA strand is missing.
    print(build_complement('ATGCAT'))  # TACGTA
    print(build_complement('GCTATAC'))  # CGATATG


def build_complement(dna):
    """
    :param dna: str, capital string consists of "ATGC"
    return: str, error message or corresponding DNA pair
    """
    sup = ""
    if len(dna) == 0:
        # True scope: empty string
        return "DNA strand is missing."
    else:
        # False scope: length parameter (str) is NOT 0
        for i in range(len(dna)):
            # for loop scope: loop as many times as the length of the dna string
            nitrogenous_base = dna[i]
            if nitrogenous_base == "A":
                # if statement scope: replace the nitrogenous_base in the original DNA strand
                # with its supplementary nitrogenous_base
                sup = sup + "T"
            elif nitrogenous_base == "T":
                sup = sup + "A"
            elif nitrogenous_base == "G":
                sup = sup + "C"
            elif nitrogenous_base == "C":
                sup = sup + "G"
        return sup


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
