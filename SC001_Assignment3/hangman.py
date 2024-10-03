"""
File: hangman.py
Name: 李名翔 Thomas
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. display the current word
    2. show user how many wrong guesses left
    3. if wrong guesses left > 0:
        get a letter from user
    4. judge if that letter is Illegal:
        if Illegel, return Illegal format, wrong guesses left remains the same
    5. wrong guesses left -1, check if that letter is in answer
        if it is in answer, update the display
    """
    wrong_guesses_left = N_TURNS  # initial wrong guesses left = N_TURNS
    answer = random_word()  # get a random word as answer

    # print initial status of the word before any guesses
    print("The word looks like: ", end="")
    for i in range(len(answer)):
        print("-", end="")
    print("\nYou have " + str(wrong_guesses_left) + " wrong guess left.")
    # print the initial number of wrong guesses left
    current_display = first_display(len(answer))
    # use "first_display" function to return current display of word

    while wrong_guesses_left > 0:
        #  while loop scope: user still has > 0 wrong guesses left
        input_ch = input("Your guess: ").upper()  # get a guess from user
        if not input_ch.isalpha():
            # True scope: user input is not an alhabet, print Illegal message
            print("Illegal format.")
        elif len(input_ch) != 1:
            # True scope: user input is not one alphabet, print Illegal message
            print("Illegal format")
        else:
            # False scope: user innput is legal
            if input_ch not in answer:
                # True scope: wrong guess, print a message, wrong guesses left - 1
                print("There is no " + input_ch + "'s in the word.")
                wrong_guesses_left -= 1
            else:
                # False scope: correct guess, print a message
                print("You are correct!")

            new_display = display(answer, input_ch, current_display)
            current_display = new_display  # duplicate the current display, so the current can be changed

            if new_display.find("-") == -1:
                # True scope: there is no "-" in display, user guessed the answer
                print("You win!!")
                print("The answer is: " + answer)
                return
            elif wrong_guesses_left != 0:
                # True scope: user still has a chance to guess
                print("The word look like this: " + new_display)
                print("You have " + str(wrong_guesses_left) + " wrong guess left.")

    if wrong_guesses_left < N_TURNS:
        # True scope: user runs out of guesses
        print("You are completely hung :(")
        print("The answer is: " + answer)


def first_display(num):
    """
    :param num: int, number of alphabets in the word
    return result: str, turn word into -'s
    """
    result = ""
    for i in range(num):
        result += "-"
    return result


def display(answer, input_ch, current_display):
    """
    :param answer: str, answer of the hang man game
    :param input_ch: str, user's guess
    :param current_display: str, the current status of the display
    return: new display: str, new display after a correct guess
    """
    new_display = current_display  # store current display in new_display
    temp_answer = answer  # store answer in tempporary answer
    for ch in answer:
        # for loop scope: check every character in answer
        if input_ch == ch:
            # True scope: user input == answer's character
            new_display = replace(new_display, temp_answer.find(ch), input_ch)  # replace "-" in answer with user input
        temp_answer = replace(temp_answer, temp_answer.find(ch), "#")  # replace character in tempporary answer with "#"
    return new_display


def replace(old_str, index, input_ch):
    """
    :param old_str: str, old string that some of its characters need to be replaced
    :param index: str, index of the character that need to be replaced
    :param input_ch: str, character user wants to replace with
    return new_str: str, new string after replacing
    """
    front = old_str[:index]
    end = old_str[index + 1:]
    return front + input_ch + end


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
