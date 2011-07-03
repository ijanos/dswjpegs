# -*- coding: utf-8 -*-

"""
Rename the files based on the exif date
"""

import sys
import os

import pyexiv2

def getMetadata(f):
    metadata = pyexiv2.ImageMetadata(f)
    metadata.read()
    return metadata

def getDate(file):
    metadata = getMetadata(file)
    print file,
    try:
        datetag = metadata['Exif.Image.DateTime']
        print datetag.value.strftime("%Y/%Y-%m-%d/%Y%m%d-%H%M")
    except KeyError:
        print "Missing date"


#def rename(f):
#    path = getDate(f)

def traverseDir(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = name.split('.')[-1].lower()
            if  ext == 'jpg' or ext == 'jpeg':
                getDate(os.path.join(root, name))

def main():
    d = sys.argv[1]
    traverseDir(d)

if __name__ == "__main__":
    main()
