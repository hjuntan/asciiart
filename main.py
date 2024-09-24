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

def main():
    image = get_image()
    
    # Display the image
    image.show()

    height, width = image.size
    print(f"Image size: {height}x{width}")

main()