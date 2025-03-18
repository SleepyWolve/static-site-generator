import os
import shutil

def copy_static_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            copy_static_recursive(s, d)
        else:
            shutil.copy2(s, d)