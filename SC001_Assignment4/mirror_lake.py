"""
File: mirror_lake.py
Name: 李名翔 Thomas
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the filepath of the image user wants to highlight
    :return: SimpleImage, a mirror image of the original image
    """
    img = SimpleImage(filename)
    # make a blank canvas, but height is 2 times bigger than the original image
    img_mirror = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            img_mirror_p1 = img_mirror.get_pixel(x, y)  # upper part of the canvas
            img_mirror_p2 = img_mirror.get_pixel(x, img_mirror.height - 1 - y)  # lower part of the canvas

            # p1 copies the original image
            img_mirror_p1.red = img_p.red
            img_mirror_p1.green = img_p.green
            img_mirror_p1.blue = img_p.blue

            # p2 copies the original image, but y in reversed order
            img_mirror_p2.red = img_p.red
            img_mirror_p2.green = img_p.green
            img_mirror_p2.blue = img_p.blue
    return img_mirror


def main():
    """
    show the image that user wants to process
    then call the "reflect" function to generate a mirror image
    show the mirror image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
