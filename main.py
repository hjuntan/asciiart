import os, sys
import math
from PIL import Image

def get_image():
    # Get the path to the image
    try:
        image_path = sys.argv[1]
    except IndexError:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    # Open the image
    image = Image.open(image_path)

    return image


def get_scale():
    # Get the scale
    file = open("scale.txt", "r")
    scale = file.read().splitlines()
    file.close()

    return scale

def custom_grayscale(image):
    # Custom grayscale conversion
    width, height = image.size
    grayscale_image = Image.new("L", (width, height))
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
            else:  # RGB
                r, g, b = pixel
            # Custom formula for grayscale conversion
            gray = int((r + g + b) / 3)
            grayscale_image.putpixel((x, y), gray)
    return grayscale_image

def process_image(image, scale):
    # Convert the image to grayscale
    # Either use the custom grayscale conversion or the built-in one

    #image = image.convert("L") # Built-in grayscale conversion
    image = custom_grayscale(image) # Custom grayscale conversion

    # Resize the image to fit within the terminal. 
    # Change these to change the resolution of the output
    max_width = 400  # Adjust this value based on your terminal width
    max_height = 200  # Adjust this value based on your terminal height

    # Calculate the new dimensions while maintaining the aspect ratio
    aspect_ratio = image.width / image.height
    if image.width > max_width:
        new_width = max_width
        new_height = int(max_width / aspect_ratio)
    else:
        new_width = image.width
        new_height = image.height

    if new_height > max_height:
        new_height = max_height
        new_width = int(max_height * aspect_ratio)

    # Resize the image
    image = image.resize((new_width, new_height))
    return image


def print_image(image, scale):
    width, height = image.size
    print(f"Image size: {height}x{width}")

    # Print the pixel values
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            brightness = math.floor(pixel * len(scale) / 256)
            print(scale[brightness] * 2, end="")
        print()


def main():
    image = get_image()
    scale = get_scale()

    # Process the image
    image = process_image(image, scale)

    print_image(image, scale)


main()
