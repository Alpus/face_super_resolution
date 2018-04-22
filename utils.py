import os
import shutil


def maybe_mkdir(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def remove_if_exists(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
        
def get_last_file(folder):
    return list(sorted(os.listdir(folder)))[-1]
