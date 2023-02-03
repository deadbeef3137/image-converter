***
### Autor: [@deadbeef3137](https://github.com/deadbeef3137)
***

# Image Converter

## Overview
This program allows you to convert images in PNG, JPG, GIF, BMP, and other formats to any other image format compatible with the Python Imaging Library (PIL).

## Usage
Using the program is simple, first you must have Python installed on your computer. Then, download the image_converter.py file and run it in the terminal or command line.
```
python image_converter.py
```

## Input
By default, the program will look for images in the same directory where the image_converter.py file is located. The converted images will be saved in a folder called ico_files in the same directory.

```
python image_converter.py
```

In addition, the user can specify the output image size using the -s or --size parameter. If a size is specified, the image will be resized to that size before being saved. If full is specified, the image will be saved in its original size.

```
python image_converter.py -s 128
```

## Output
The program also allows you to specify the output format. To do this, you can use the following structure:
```
python image_converter.py -s 128 -f png
```

The converted images will be saved in a folder with the name of the output format followed by "_files" in the same directory. For example, if the output format is PNG, the images will be saved in a folder called "png_files".

## Requirements
- Python 3.x
- Python Imaging Library (PIL)

To install the PIL library, run in the terminal or command line:

```
pip install pillow
```
