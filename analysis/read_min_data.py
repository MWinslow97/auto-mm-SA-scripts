#!/usr/bin/env

import os
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display


size = 0                                    #initiator for list size
files = ['1min.out']                        #file data will be taken from
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        c = int(text.count('NSTEP'))        #counts how many times NSTEP appears in output
        size += c-1                         #determines size of list


step = np.zeros(size)                       #creates list of desired size
energy = np.zeros(size)                     #populates list with 0's

n = 0                                       #counter to iterate through list
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        results = re.split('RESULTS|TIMINGS', text)[1]  #reads through results section of output
        lines = results.split('\n')
        for pos, i in enumerate(lines):
            if 'NSTEP' in i and n<=size:                #records data from line after NSTEP appears (check output file format)
                line = lines[pos+1]
                words = line.split()
                np.put(step, n, float(words[0]))
                np.put(energy, n, float(words[1]))
                n += 1


d = {'Step': step, 'Energy': energy}
df = pd.DataFrame(data=d)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)
df.plot(x = 'Step', y = 'Energy')
plt.show()

