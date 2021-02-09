from image.color import Color
from renderer.material import Material
from renderer.light import Light
from geometry.point import Point
from geometry.sphere import Sphere
from linalg.vector import Vector

WIDTH = 320
HEIGHT = 200
RENDERED_IMG = "red_ball.ppm"
CAMERA = Vector(0, 0, -1)
OBJECTS = [Sphere(Point(0, 0, 0), 0.5, Material(Color.from_hex("#FF0000")))]
LIGHTS = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF"))]
