"""
File: similarity.py (extension)
Name: 李名翔 Thomas
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    1. get a DNA sequence (long) from user
    2. get another DNA sequence (short) to match
    3. match the short DNA sequence with the whole DNA sequence, and calculate its similarity
    4. print the DNA sequence of the biggest similarity
    """
    long_sequence = input("Please give me a DNA sequence to match: ").upper()  # get long sequence from user
    short_sequence = input("What DNA sequence would you like to match ").upper()  # get short sequence from user
    print("The best match is " + match_dna(long_sequence, short_sequence).upper())  # print the most similar sequence


def match_dna(long_sequence, short_sequence):
    """
    :param long_sequence: str, the sequence which the user wants to match (long)
    :param short_sequence: str, the sequence which the user wants to match (short)
    return max_score_sequence: str, the matched sequence with highest similarity
    this function compares every segment of the long sequence with the short sequence
    and returns the segment with the highest similarity
    """
    max_score = 0
    max_score_sequence = ""
    for i in range(len(long_sequence) - len(short_sequence) + 1):
        long_sequence_sliced = long_sequence[i:i + len(short_sequence)]
        """
        for loop scope: cut the long sequence into segments,
        e.g.:
            long sequence == "ABCDDCBA"
            short sequence == "BAD", length of short sequence is 3
            segments == "ABC", "BCD", "CDD", "DDC", "DCB", "CBA"
        number of segments == length of long sequence - length of short sequence + 1
        """
        score = 0

        for j in range(len(short_sequence)):
            # for loop scope: compare every nitrogen base in the sliced long sequence with the short sequence
            if long_sequence_sliced[j] == short_sequence[j]:
                # True scope: nitrogen bases in these two sequence are the same, score + 1
                score += 1
        if score > max_score:
            # True scope: current score is higher than current max score, assign new max score
            max_score = score
            max_score_sequence = long_sequence_sliced
    return max_score_sequence


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
