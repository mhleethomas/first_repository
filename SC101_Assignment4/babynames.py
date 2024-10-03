"""
File: babynames.py
Name: Ming-Hsiang (Thomas), Lee
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank.
        This function does not return any value.
    """

    # True scope: name (str) is NOT in name_data (dict)
    if name not in name_data:
        name_data[name] = {year: rank}  # name_data = {name: {year: rank}}

    # False scope: name (str) already in name_data (dict)
    else:
        # True scope: a new year-rank pair for this name, or a higher rank (smaller number) for this year
        if year not in name_data[name] or int(rank) < int(name_data[name][year]):
            year_rank_dictionary = name_data[name]  # {year: rank}
            year_rank_dictionary[year] = rank  # {year: rank, year2: rank2}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """

    line_index = 0
    with open(filename, "r") as f:
        # for each loop: loop through every line in the file
        for line in f:
            line_index += 1
            stripped_line = line.strip()

            # True scope: first line, containing year
            if line_index == 1:
                year = stripped_line
            # False scope: all lines except first line, split into tokens with ","
            else:
                tokens = stripped_line.split(",")

                # remove " " in tokens (list) and put them all in a new list
                cleaned_tokens = []
                # for each loop: remove " " in tokens
                for token in tokens:
                    cleaned_token = ""
                    # for each loop: remove every " " in a token,
                    for character in token:
                        if character != " ":
                            cleaned_token += character
                    cleaned_tokens.append(cleaned_token)

                # populates the name_data dict (cleaned_tokens[1] for male, cleaned_tokens[2] for female)
                add_data_for_name(name_data, year, cleaned_tokens[0], cleaned_tokens[1])
                add_data_for_name(name_data, year, cleaned_tokens[0], cleaned_tokens[2])


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []

    # for each loop: loop over name_data
    for name, year_rank_dict in name_data.items():
        # for loop scope: slice name into name_pieces, with the length of target, and compare it to the target
        for i in range(len(name) - len(target) + 1):
            name_pieces = name[i:i + len(target)]
            # True scope: append names which include target to matching_names[]
            if name_pieces.lower() == target.lower():
                matching_names.append(name)

    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
