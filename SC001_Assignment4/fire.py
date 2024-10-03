"""
File: fire.py
Name: 李名翔 Thomas
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the filepath of the image user wants to highlight
    :return: SimpleImage, the highlighted image
    """
    img = SimpleImage(filename)
    for pixel in img:
        # for each loop scope: loop through every pixel in image
        avg = (pixel.red + pixel.green + pixel.blue) // 3  # calculate the average of the RGB values
        if pixel.red > avg * HURDLE_FACTOR:
            # True scope: meets the condition of highlight, make pixels red
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # False scope: does NOT meet the condition, make pixels into grey scale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    show the image that user wants to process
    then call the "highlight_fires" function to highlight the fire area
    show the image after processing
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
