# Split a directory of photos into smaller sized directories, for easier backup
#
# Note: this is a horribly naive implementation, depending on that the files 
# feeded to it will be small (few megabytes) and mostly the same size.

import os
import sys
import shutil

CDR80 = 737000000 # 737,280,000 bytes
DVD47 = 4700000000 # DVD-R size: 4,707,319,808 bytes

class Backup_unit:
    def __init__(self,name):
        self.name = name
        self.file_list = []
        self.size = 0

    def put(self,f):
        fsize = os.path.getsize(f)
        self.size += fsize
        self.file_list.append(f)

    def __repr__(self):
        reprstr = '<%s %d bytes %s>' % (self.name, self.size, self.file_list)
        return reprstr

    def print_txt(self):
        for filename in self.file_list:
            print self.name + " " + filename

    def copy_files(self,destdir):
        for source in self.file_list:
            filename = os.path.basename(source)
            originaldir = os.path.dirname(source)
            dest = os.path.join(destdir,self.name,originaldir)
            if not os.path.exists(dest):
                try:
                    os.makedirs(dest)
                except OSError:
                    pass
            dest = os.path.join(dest,filename)
            shutil.copyfile(source,dest)

    def move_files(self):
        pass

class Backup:
    def __init__(self, startdir, size = DVD47):
        self.sizelimit = size
        self.newname = get_new_dir("dvd-",1)
        self.units = [Backup_unit(self.newname())]
        traverseDir(startdir, self.addFile)
        
    def addFile(self, filepath):
        size = os.path.getsize(filepath)
        current_unit = self.units[-1]
        if ((current_unit.size + size) > self.sizelimit):
            self.units.append(Backup_unit(self.newname()))
            current_unit = self.units[-1]
        current_unit.put(filepath)

    def copy(self, destdir):
        for unit in self.units:
            unit.copy_files(destdir)
            

def traverseDir(directory, fun):
    """
    Walk the directory and its subdirectories and look for files 
    ending with .jpg and .jpeg (case insensitive) 
    """
    for root, dirs, files in os.walk(directory):
        for name in files:
            ext = name.split('.')[-1].lower()
            if  ext == 'jpg' or ext == 'jpeg':
                f = os.path.join(root, name)
                fun(f)

def get_new_dir(basename, counter_start):
    counter = [counter_start]
    def closure():
        new_name = basename + str(counter[0])
        counter[0] += 1
        return new_name
    return closure

if __name__ == "__main__":
    srcdirectory = sys.argv[1]
    destdir = sys.argv[2]
    b = Backup(srcdir)
    b.copy(destdir)
