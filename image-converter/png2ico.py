import argparse
import os
import glob
from PIL import Image, ImageOps

def convert_image(input_file, output_file, size, output_format):
    with Image.open(input_file) as img:
        if size == "full":
            img.save(output_file, format=output_format)
        else:
            img = ImageOps.fit(img, (size, size), method=Image.Resampling.LANCZOS)
            img.save(output_file, format=output_format)

def batch_convert(input_folder, output_folder, size, output_format):
    input_files = glob.glob(input_folder + "/*.*")
    for input_file in input_files:
        try:
            with Image.open(input_file) as img:
                filename, extension = os.path.splitext(input_file)
                output_file = output_folder + "/" + os.path.basename(filename) + "." + output_format
                convert_image(input_file, output_file, size, output_format)
        except OSError:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="The size of the output image", default="full")
    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = script_dir
    output_format = input("Enter the output format (e.g. jpg, png, bmp, ico): ")
    output_folder = os.path.join(input_path, output_format + "_files")
    os.makedirs(output_folder, exist_ok=True)
    size = args.size

    if os.path.isfile(input_path):
        try:
            with Image.open(input_path) as img:
                filename, extension = os.path.splitext(input_path)
                output_file = os.path.join(output_folder, os.path.basename(filename) + "." + output_format)
                convert_image(input_path, output_file, size, output_format)
        except OSError:
            print("The input file is not a supported image format")
    elif os.path.isdir(input_path):
        batch_convert(input_path, output_folder, size, output_format)
    else:
        print("The input is not a valid file or folder")
