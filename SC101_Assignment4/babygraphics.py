"""
File: babygraphics.py
Name: Ming-Hsiang (Thomas), Lee
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940,
         1950, 1960, 1970, 1980, 1990,
         2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return int((width - 2 * GRAPH_MARGIN_SIZE) * int(year_index) / len(YEARS)) + GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """

    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # create 2 horizontal lines at top & bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # for loop scope: create vertical lines, amount is equal to len(YEARS)
    for spacing in range(0,
                         CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE,
                         (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + spacing, 0,
                           GRAPH_MARGIN_SIZE + spacing, CANVAS_HEIGHT)

    # for loop scope: create year texts for all years in YEARS[]
    for year_index in range(len(YEARS)):
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """

    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # for loop scope: handle every name which user wants to look up
    for name_index in range(len(lookup_names)):
        lookup_name = lookup_names[name_index]

        # assign the color of line
        color = COLORS[name_index % 4]

        # True scope: have data of lookup_name
        if lookup_name in name_data:
            # use lookup_name as key to get its value in name_data
            year_rank_dict = name_data[lookup_name]

            # for each loop: make sure no data missing in any year
            for year in YEARS:
                # True scope: if data missing in year_rank_dict, then assign MAX_RANK to its rank
                if str(year) not in year_rank_dict:
                    year_rank_dict[str(year)] = str(MAX_RANK)

            # TODO: because I dont know how to work with dictionary properly, so I create 2 lists :(
            year_list = []
            rank_list = []
            for year, rank in sorted(year_rank_dict.items()):
                year_list.append(year)
                rank_list.append(rank)

            # for loop scope: draw lines between canvas (x: year, y: rank)
            for i in range(len(YEARS) - 1):
                # True scope: calculate the coordinate, and connect them to draw lines
                x1 = get_x_coordinate(CANVAS_WIDTH, i)
                y1 = int(rank_list[i]) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000 + GRAPH_MARGIN_SIZE
                x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)
                y2 = int(rank_list[i + 1]) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000 + GRAPH_MARGIN_SIZE
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

            # for loop scope: add name-rank texts next to all data points
            for i in range(len(YEARS)):
                x = get_x_coordinate(CANVAS_WIDTH, i)
                y = int(rank_list[i]) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000 + GRAPH_MARGIN_SIZE

                # True scope: add name next to ranking, and replace ranking (>=MAX_RANK) with "*"
                if int(rank_list[i]) >= MAX_RANK:
                    show_text = lookup_name + " *"
                # False scope: add name next to ranking
                else:
                    show_text = lookup_name + " " + rank_list[i]
                canvas.create_text(x + TEXT_DX, y, text=show_text, anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
