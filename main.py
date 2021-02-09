#!/usr/bin/env python
"""A pure Python ray tracer.

Based on a tutorial by Arun Ravindran, <https://www.youtube.com/playlist?list=PL8ENypDVcs3H-TxOXOzwDyCm5f2fGXlIS>

author: Sylvain Laporte
date: 2021-02-07
"""

import argparse
import importlib
import os
from multiprocessing import cpu_count, process

from renderer.engine import RenderEngine
from renderer.scene import Scene


def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "scene", help="Path to scene file (without .py extension)")
    parser.add_argument("-p", "--processes", action="store", type=int,
                        dest="processes", default=0, help="Number of processes (0 = auto)")
    args = parser.parse_args()

    # Setting the number of processes to uses
    if args.processes == 0:
        process_count = cpu_count()
    else:
        process_count = args.processes
    print(f"Process count={process_count}")

    # Import the scene description
    scn_desc = importlib.import_module(args.scene)

    scene = Scene(
        scn_desc.CAMERA,
        scn_desc.OBJECTS,
        scn_desc.LIGHTS,
        scn_desc.WIDTH,
        scn_desc.HEIGHT
    )
    engine = RenderEngine()

    os.chdir(os.path.dirname(os.path.abspath(scn_desc.__file__)))
    with open(scn_desc.RENDERED_IMG, "w") as img_fileobj:
        engine.render_multiprocess(scene, process_count, img_fileobj)


if __name__ == "__main__":
    main()
