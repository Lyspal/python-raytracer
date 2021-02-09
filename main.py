#!/usr/bin/env python
"""A pure Python ray tracer.

Based on a tutorial by Arun Ravindran, <https://www.youtube.com/playlist?list=PL8ENypDVcs3H-TxOXOzwDyCm5f2fGXlIS>

author: Sylvain Laporte
date: 2021-02-07
"""

import argparse
import importlib
import os

from renderer.engine import RenderEngine
from renderer.scene import Scene


def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "scene", help="Path to scene file (without .py extension)")
    args = parser.parse_args()
    scn_desc = importlib.import_module(args.scene)

    scene = Scene(
        scn_desc.CAMERA,
        scn_desc.OBJECTS,
        scn_desc.LIGHTS,
        scn_desc.WIDTH,
        scn_desc.HEIGHT
    )
    engine = RenderEngine()
    image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(scn_desc.__file__)))
    with open(scn_desc.RENDERED_IMG, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
