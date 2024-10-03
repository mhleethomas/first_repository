"""
File: stanCodoshop.py
Name: 李名翔 Thomas
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
type "py stanCodoshop.py" + "folder name" in the terminal to process
    for example: py stanCodoshop.py hoover
if not working, try typing "python stanCodoshop.py" + "folder name" in the terminal to process
    for example: python stanCodoshop.py hoover
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** (1 / 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_red = 0
    total_green = 0
    total_blue = 0

    # for loop scope: calculate the total value of RGB for each piexl, separately
    for i in range(len(pixels)):
        total_red += pixels[i].red
        total_green += pixels[i].green
        total_blue += pixels[i].blue

    return [total_red // len(pixels), total_green // len(pixels), total_blue // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels,
    returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    shortest_dist = float("inf")
    best = pixels[0]

    # for loop scope: to compare the color distant of each pixel, and keep the pixel with the shortest color distant
    for i in range(len(pixels)):
        # average is a list, consist of the average [r, g, b] value of the pixels from different image
        average = get_average(pixels)
        pixel_dist = get_pixel_dist(pixels[i], average[0], average[1], average[2])  # calculate the color distant

        # True scope: color distant we got is less than the current shortest color distant
        if pixel_dist < shortest_dist:
            shortest_dist = pixel_dist  # re-assign the new shotest color distant
            best = pixels[i]  # best pixel is the i-th pixel
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # double for loop scope: go through each pixel in a image
    for x in range(result.width):
        for y in range(result.height):
            pixels_at_x_y = []  # new pixels list for new (x, y)

            # for loop scope: go through each image in the images[]
            for image in images:
                pixel_at_x_y = image.get_pixel(x, y)  # pixel at (x, y)
                pixels_at_x_y.append(pixel_at_x_y)  # add 1 pixel to pixel_at_x_y[]

            # assign the rgb value of best pixel to the result blank canvas
            best = get_best_pixel(pixels_at_x_y)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue

    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
