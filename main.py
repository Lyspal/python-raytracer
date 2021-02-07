#!/usr/bin/env python
"""A pure Python ray tracer.

Based on a tutorial by Arun Ravindran, <https://www.youtube.com/playlist?list=PL8ENypDVcs3H-TxOXOzwDyCm5f2fGXlIS>

author: Sylvain Laporte
date: 2021-02-07
"""

from image.image import Image
from image.color import Color


def main():
    WIDTH = 3
    HEIGHT = 2
    im = Image(WIDTH, HEIGHT)
    red = Color(x=1, y=0, z=0)
    green = Color(x=0, y=1, z=0)
    blue = Color(x=0, y=0, z=1)

    im.set_pixel(0, 0, red)
    im.set_pixel(1, 0, green)
    im.set_pixel(2, 0, blue)

    im.set_pixel(0, 1, red + green)
    im.set_pixel(1, 1, red + blue + green)
    im.set_pixel(2, 1, red * 0.001)

    with open("test.ppm", "w") as img_file:
        im.write_ppm(img_file)


if __name__ == "__main__":
    main()
