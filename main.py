#!/usr/bin/env python
"""A pure Python ray tracer.

Based on a tutorial by Arun Ravindran, <https://www.youtube.com/playlist?list=PL8ENypDVcs3H-TxOXOzwDyCm5f2fGXlIS>

author: Sylvain Laporte
date: 2021-02-07
"""

from image.color import Color
from linalg.vector import Vector
from geometry.point import Point
from geometry.sphere import Sphere
from renderer.scene import Scene
from renderer.engine import RenderEngine


def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
