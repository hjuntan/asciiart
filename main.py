import os, sys
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
    scale = file.read().split('\n')
    file.close()

    print("Scale:" + scale[0])

    return scale

def main():
    image = get_image()

    scale = get_scale()

    # Convert the image to grayscale
    image = image.convert("L")

    width, height = image.size
    print(f"Image size: {height}x{width}")

    # Print the pixel values
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            print(f"{pixel:3}", end=" ")
        print()

    # Display the image
    image.show()

main()