"""
Example usage:
    - python scripts/create_gif.py plot_*.png
    - python scripts/create_gif.py plot_1.png plot_2.png plot_3.png
    - python scripts/create_gif.py plot_{1..3}.png
    - png_files=""
      for i in $(seq 0 2 100); do
        png_files+="plot_$(printf "%04d" $i).png "
      done
      eval python scripts/create_gif.py $png_files
    - png_files=()
      for i in $(seq 0 2 100); do
        png_files+=("plot_$(printf "%04d" $i).png")
      done
      python scripts/create_gif.py "${png_files[@]}"
"""

from PIL import Image
import sys
import os
import argparse

os.makedirs("output", exist_ok=True)

parser = argparse.ArgumentParser(description="Create a GIF from PNG files.")
parser.add_argument("png_files", nargs="+", help="PNG files to create the GIF from")
parser.add_argument(
    "--fps", type=int, default=30, help="Frames per second (default: 30)"
)

args = parser.parse_args()
png_files = args.png_files
fps = args.fps

if not png_files:
    print("Error: No PNG files provided.")
    sys.exit(1)

duration = int(1000 / fps)  # Duration is in milliseconds

frames = [Image.open(f) for f in png_files]

# get the filenames of the png files (without the extension and path)
png_filenames = [f.split("/")[-1].split(".")[0] for f in png_files]
output_filename = f"{png_filenames[0]}-{png_filenames[-1]}-{fps}fps.gif"

frames[0].save(
    f"output/{output_filename}",
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=duration,
    loop=0,
)

print(f"Created GIF: output/{output_filename}, file size: {os.path.getsize(f'output/{output_filename}') / 1024 / 1024:.2f} MB")
