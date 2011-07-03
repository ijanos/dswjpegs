# -*- coding: utf-8 -*-

"""
Mass-fill JPEG's EXIF/IPTC tags based on the file's path
"""

import sys
import os

import pyexiv2

Verbose = True
Write   = False

def traverseDir(dir):
    """
    Walk the directory and its subdirectories and look for files 
    ending with .jpg and .jpeg (case insensitive) and sets the IPTC
    Keywords tags based on the path
    """
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = name.split('.')[-1].lower()
            if  ext == 'jpg' or ext == 'jpeg':
                f = os.path.join(root, name)
                setMetadata(f,getTagsFromPath(f))

def getMetadata(f):
    metadata = pyexiv2.ImageMetadata(f)
    metadata.read()
    if 'Iptc.Application2.Keywords' in metadata.iptc_keys:
        tags = metadata['Iptc.Application2.Keywords'].value
    else:
        tags = []
    return (metadata, tags)

def ppTagList(file, taglist):
    """
    Prettyprint the list of tags
    """
    print file
    for tag in taglist:
        print tag + ";",
    print "\n"

def setMetadata(f,tags):
    (md, current) = getMetadata(f)
    new = list(set(current + tags)) # remove duplicates
    if '' in new: # drop the empty tag, if exists
        new.remove('')
    if Verbose:
        ppTagList(f,new)
    if Write:
        md['Iptc.Application2.Keywords'] = new
        md.write()

def getTagsFromPath(p):
    p0 = unicode(p, encoding="utf-8")
    tags = os.path.split(p0)[0].split("/")
    return tags

def usage():
    pass

def main():
    d = sys.argv[1]
    traverseDir(d)

if __name__ == "__main__":
    main()
