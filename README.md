# Project 2: ASCII Art

This is a short project made during a computer vision class I am taking in GWU.
To try out this program, clone this repository and in the file directory, run:
```bash
$ python main.py <your-file-path>
```
where <your-file-path> is the file path of your image.

## Problem Domain and Project Description

I was curious on how to develop a system that transform visual images into ASCII art, a form of text-based imagery where the pixels of an image are replaced with characters, and compare the difference in "quality" between them. This project might strike an interest for artists, developers, and enthusiasts interested in digital art, retro computing. Example inputs include photographs, illustrations, and digital art, while outputs are ASCII conversions that maintain recognizable features and artistic integrity of the original images.

## Detailed Description of Approach

This project involves two major parts, converting the image into a greyscale version of itself, and mapping the intensity of those greyscale pixels to their corresponding ASCII characters, which vary in visual density.

The way to convert the image into greyscale is quite diverse: averaging the R, G and B values, taking a weighted average of the values, etc (lots more details [here](https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color)). The two main ways I convert the image into greyscale is: 
> using the build-in greyscale convertor from [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert), 
> and using a "custom" scale using the average of the R, G and B values: (R + G + B) / 3.

You can change different greyscale convertor by setting the `custom_grayscale` boolean and this section:
```python
            # Custom formula for grayscale conversion
            gray = int((r + g + b) / 3)
            grayscale_image.putpixel((x, y), gray)
```

There are different brightness scale of ASCII characters. I used the brightness scale posted [here by chungaloider](https://stackoverflow.com/questions/30097953/ascii-art-sorting-an-array-of-ascii-characters-by-brightness-levels-c-c).

You can change the brightness scale by changing the __scale.txt__ file found within the repository.

### Challenge 1: Image printed are "squished"

During this project, I noticed that the image printed is "squished", as it was slimmed down. This is due to the representation of character being rectangular as opposed to the square shape of pixels.

![Squished picture vs original](/images/comparision-squished-vs-unsquished.png)

An easy fix is to double or triple each character every time it was printed.

![Unsquished image](/images/unsquished.png)

### Challenge 2: Overflow of characters in a line

One aspect of this project I found surprising tough is the limitation of printing characters in the terminal, as there is limit on how much characters can be printed out on a single line before it will overflow towards the next line.

![Character overflow](/images/overflow-characters.png)

One ways to overcome this issue is making a max limit on the height and width. If the width exceeds the set limit, resize the image using Pillow's in-build [resize](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize) function. Same goes for height. You can change the `max_width` and `max_height` found within the code.

One additional thing:
> You can change the printing output to a __txt__ file instead of printing them on the terminal by simply changing the boolean `file_print`. This way, you can share the txt file instead of screenshotting the final image.

## Results and Comparison

When compared to the original images, the ASCII art produced by our model retains a high level of visual integrity.

![Sample zebra](/images/sample.txt) ![Original zebra](/images/zebra.jpg)

Nevertheless, there are drawbacks, like the loss of detail in extremely complicated images, which could be fixed by improving the model's sensitivity to subtle tonal changes, adding colour in future iterations, or even improving pixel detection, for instance:

Even though this project successfully shows that automated ASCII art generation is feasible for many applications, more work is required to produce outputs that are professional-grade, especially in areas like real-time processing and dynamic resolution scaling.