from image.color import Color
from renderer.material import Material, CheckerMaterial
from renderer.light import Light
from geometry.point import Point
from geometry.sphere import Sphere
from linalg.vector import Vector

WIDTH = 320
HEIGHT = 200
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    # Ground plane
    Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        CheckerMaterial(
            color1=Color.from_hex("#420500"),
            color2=Color.from_hex("#E6B87D"),
            ambient=0.2,
            reflection=0.2
        )
    ),
    # Blue ball
    Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    # Pink ball
    Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980")))
]
LIGHTS = [
    Light(Point(1.5, -0.5, -10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6")),
]
