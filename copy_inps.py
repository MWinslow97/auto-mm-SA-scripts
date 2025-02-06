#!/usr/bin/env

import shutil
import os

def copy_inp():
    path = []
    with open("path_list.txt", "r") as f:
        text = f.read().splitlines()
        for i in text:
            path.append(i)
    src_dir = '/home/pczmw1/my_scripts/md_inps'
    files = os.listdir(src_dir)
    for p in path:
        for j in files:
            source = f"{src_dir}/{j}"
            shutil.copy(source, p)

# copy_inp()
