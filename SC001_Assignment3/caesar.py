"""
File: caesar.py
Name: 李名翔 Thomas
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    1. get a SECRET NUMBER from user
    2. get a CIPHERED STRING from user
    3. execute the decipher function
    4. print the deciphered string
    """
    secret_number = int(input("Secret number: "))
    ciphered_string = str(input("What's the ciphered string?")).upper()
    print("The dsciphered string is: " + decipher(secret_number, ciphered_string))  # print the result


def decipher(sn, cs):
    """
    :param sn: int, secret number from user
    :param cs: str, ciphered string from user
    return ans: str, deciphered string
    this function shifts the ALPHABET list towards right,
        the step it shifts is determinated by the secret number
    decompose the ciphered string and look up its index in new alphabet list
    use this index to look up again, but in ALPHABET list
    use a for loop to get the deciphered string, and return ans
    """
    ans = ""  # start with a empty string
    new_alphabet = ALPHABET[-sn:] + ALPHABET[:26 - sn]  # shift the ALPHABET list using the sectet number, sn
    for i in cs:
        # for each loop scope: loop through every character in ciphered string, cs
        if i in ALPHABET:
            # True scope: the character is in the ALPHABET list
            num_in_new = new_alphabet.find(i)  # find the character's index in new alphabet list
            new_char = ALPHABET[num_in_new]  # look up new character in ALPHABET list using the index
            ans += new_char  # add a new character to ans
        else:
            # False scope: the character is not in the ALPHABET list
            ans += i  # do NOT add a new character to ans, keep the original character in the ciphered string
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
