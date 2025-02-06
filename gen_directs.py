#!/usr/bin/env

import os

def gen_directs(paths: str):
    path = []
    with open(paths, 'r') as f:
        text = f.read().splitlines()
        for i in text:
            path.append(i)
#    print(path)
    for i in path:
        try:
            os.makedirs(str(i))
            print(f"made {i}")
        except FileExistsError:
            print(f"{i} exists")
        except PermissionError:
            print(f"{i} not allowed")
        except Exception as e:
            print(f"error {e} for {i}")

# gen_directs('path_list.txt')
