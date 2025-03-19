from os import path, mkdir, listdir
from shutil import copy

def copy_static_recursive(source_dir, dest_dir):
    if not path.exists(dest_dir):
        mkdir(dest_dir)

    for item in listdir(source_dir):
        source = path.join(source_dir, item)
        dest = path.join(dest_dir, item)
        print(f" * {source} -> {dest}")
        if path.isfile(source):
            copy(source, dest)
        else:
            copy_static_recursive(source, dest)