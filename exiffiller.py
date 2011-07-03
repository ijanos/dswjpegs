# -*- coding: utf-8 -*-

"""
Mass edit exif metadata
"""

import sys

import pyexiv2

Formatstring = "%d-%m-%y_%H%M"

def getMetadata(f):
    metadata = pyexiv2.ImageMetadata(f)
    metadata.read()
    return metadata

def parseFilename(f):
    # Remove the extension from the filename
    date = string.join(f.split(".")[:-1], ".")
    parsedtime = time.strptime(date, Formatstring)
    return parsedtime

def fillDate():
    pass

def main():
    for f in sys.argv[1:]:
        print f

if __name__ == "__main__":
    main()
