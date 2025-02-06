#!/usr/bin/env

import os

def edit_inps():
    # path = []
    # temps = []
    search_txt = '= t'
    with open('temperatures.txt', 'r') as f:
        temps = f.read().splitlines()
        # for i in text:
        #     temps.append(i)
    with open("path_list.txt", "r") as f:
        path = f.read().splitlines()
        # for i in text:
        #     path.append(i)
    for i in path:
        a = i.split('/')[-1]
        b = a.split('k')[0]
        for j in temps:
            if b == j.split('.')[0]:
                replace_txt = f'= {j}'
                files = os.listdir(i)
                for k in files:
                    absolute = f'{i}/{k}'
                    with open(absolute, 'r') as f:
                        data = f.read()
                        data = data.replace(search_txt, replace_txt)
                    with open(absolute, 'w') as f:
                        f.write(data)
                


# edit_inps()
