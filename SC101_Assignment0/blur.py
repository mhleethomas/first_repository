"""
File: blur.py
Name: Ming-Hsiang (Thomas), Lee
-------------------------------
This file shows the original image first, smiley-face.png, and then compare to its blurred image.
The blur algorithm uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    1. Show the original image
    2. Blur the original image once
    3. Blur the already blurred image four more times
    4. Show the final blurred image
    """
    # Load the original image
    old_img = SimpleImage("images/smiley-face.png")
    # Display the original image
    old_img.show()

    # Blur the image once
    blurred_img = blur(old_img)

    # Blur the image four more times
    for i in range(4):
        blurred_img = blur(blurred_img)

    # Display the final blurred image
    blurred_img.show()


def blur(img):
    """
    :param img: SimpleImage, the image user wants to blur
    :return: SimpleImage, the blurred image
    """
    # Create a new blank canvas with the same dimensions as the original image
    blurred_img = SimpleImage.blank(img.width, img.height)

    # Loop through each pixel in the original image
    for x in range(img.width):
        for y in range(img.height):
            # Initialize the RGB values and the pixel count to 0
            total_r = total_g = total_b = count = 0

            # Loop through each of the neighboring pixels, including the pixel itself
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    neighbor_x = x + i
                    neighbor_y = y + j

                    # Check if the neighboring pixel is within the image bounds
                    if 0 <= neighbor_x < img.width and 0 <= neighbor_y < img.height:
                        # Get the RGB values of the neighboring pixel and add them to the totals
                        img_p = img.get_pixel(neighbor_x, neighbor_y)
                        total_r += img_p.red
                        total_g += img_p.green
                        total_b += img_p.blue
                        count += 1

            # Calculate the average RGB values
            blurred_img_p = blurred_img.get_pixel(x, y)
            blurred_img_p.red = total_r / count
            blurred_img_p.green = total_g / count
            blurred_img_p.blue = total_b / count
    return blurred_img


if __name__ == '__main__':
    main()
