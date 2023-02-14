import argparse
import os
import glob
from PIL import Image, ImageOps
from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO

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

def create_pdf(images, output_file):
    output_pdf = PdfFileWriter()
    for image in images:
        img = Image.open(image)
        bytes_io = BytesIO()
        img.save(bytes_io, format='pdf')
        pdf_file = PdfFileReader(bytes_io)
        output_pdf.addPage(pdf_file.getPage(0))
    with open(output_file, "wb") as out_stream:
        output_pdf.write(out_stream)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="The size of the output image", default="full")
    parser.add_argument("-p", "--pdf", help="Create a PDF in A4 size", action="store_true")
    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = script_dir
    output_format = input("Enter the output format (e.g. jpg, png, bmp, ico, pdf): ")
    output_folder = os.path.join(input_path, output_format + "_files")
    os.makedirs(output_folder, exist_ok=True)
    size = args.size

    if os.path.isfile(input_path):
        try:
            with Image.open(input_path) as img:
                filename, extension = os.path.splitext(input_path)
                output_file = os.path.join(output_folder, os.path.basename(filename) + "." + output_format)
                convert_image(input_path, output_file, size, output_format)
                if args.pdf:
                    pdf_file = os.path.join(output_folder, os.path.basename(filename) + ".pdf")
                    create_pdf([output_file], pdf_file)
        except OSError:
            print("The input file is not a supported image format")
    elif os.path.isdir(input_path):
        images = []
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    images.append(os.path.join(root, file))
        batch_convert(input_path, output_folder, size, output_format)
        if args.pdf:
            pdf_file = os.path.join(input_path, "output.pdf")
            create_pdf([os.path.join(output_folder, f) for f in os.listdir(output_folder)], pdf_file)
   
