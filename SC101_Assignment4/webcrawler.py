"""
File: webcrawler.py
Name: Ming-Hsiang (Thomas), Lee
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # find all "table" elements with class "t-stripe"
        # e.g.: <table class="t-stripe">
        tables = soup.find_all("table", {"class": "t-stripe"})

        # get the first element of tables[]
        table = tables[0]

        # get the text inside table element
        tbody = table.text

        # split tbody element with "\n"
        splitted_tbody = tbody.split("\n")

        # remove the unwanted data
        wanted_data = splitted_tbody[16:16 + 200 * 2]

        male_number = 0
        female_number = 0

        # for loop scope:
        for i in range(len(wanted_data)):
            # True scope: odd number lines are name with number (even number lines are "rank")
            # e.g.: Noah 183,258 Emma 194,988
            if i % 2 == 1:
                name_number_lines = wanted_data[i]
                tokens = name_number_lines.split(" ")

                # for loop scope: use string manipulation to remove the "," in numbers
                # e.g.: 183,258 ---> 183258
                formatted_male_number = ""
                for character in tokens[1]:
                    if character.isdigit():
                        formatted_male_number += character
                formatted_female_number = ""
                for character in tokens[3]:
                    if character.isdigit():
                        formatted_female_number += character

                # summation of the formatted numbers
                male_number += int(formatted_male_number)
                female_number += int(formatted_female_number)

        print(f"Male Number: {male_number}")
        print(f"Female Number: {female_number}")


if __name__ == '__main__':
    main()
