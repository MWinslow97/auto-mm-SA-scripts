#!/usr/bin/env

def gen_path(mol_names: str, temps: str):
    molecules = []
    temp = []
    path_start = '/home/pczmw1/TESTING/path_setup/'
    path_mid = '/rotorDock/pose1/'

    with open(mol_names, 'r') as f:
        text = f.read().splitlines()
        for i in text:
            molecules.append(i)
    with open(temps, 'r') as f:
        text = f.read().splitlines()
        for i in text:
            j = i.split('.')[0]
            temp.append(j)
    # p = open("path_list.txt", "w")
    paths = [str] * len(temp)*len(molecules)
    iterator = 0
    for t in temp:
        for molecule in molecules:
            path = f"{path_start}{molecule}{path_mid}{t}k"
            paths[iterator] = path
            iterator += 1
            # p.write(path + "\n")

# gen_path('molecules.txt', 'temperatures.txt')
