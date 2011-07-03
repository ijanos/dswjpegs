Do stuff with JPEGs
===================

Finally started to make some sense of my ever growing photo collection
directory. The ideas:

* Organize photos into a date based directory structure
  *yyyy/yyyy-mm-dd/yyyymmdd-hhmm.jpg*

* Tag photos

* Dont depend on any external database, store data in the images.


The scripts are written in python2 and depend on the
[pyexiv2](http://tilloy.net/dev/pyexiv2/) library. 


iptctagger.py
-------------

This script splits the path of a picture and adds each directory name as a
tag to the picture's IPTC keywords metadata field. 

My photos were in an ad-hoc directory sctructure (something like
*photos/2005summer/vacation01*) So why not use these to bootstrap the tags.

exifrenamer.py
--------------

Rename files based on ther exif creaton date.

exiffiller.py
-------------

Some of my pictures don't have an exif date, but the file name contains
information about the date and time of when the picture was taken.

vim: tw=78
