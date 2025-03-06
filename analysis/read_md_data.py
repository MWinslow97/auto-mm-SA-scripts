#!/usr/bin/env

import os
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display


size = 0                                                                                #initiazes size of lists
indiv = []                                                                              #each output starts at 0, this list will cumulatively count the total size
files = ['2heat.out', '3pressure.out', '4pressure2.out', '5equil.out', '6prod.out']     #files data to be taken from
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        c = int(text.count('NSTEP')) - 2                                                #counts number of times NSTEP appears (-2 as final two mentions are averages, check output file format)
        size += c                                                                       #total number of data points of combined files
        indiv.append(size-1)                                                            #number of data points within each file

step = np.zeros(size)                                                                   #creates lists of 0's of desired size
temp = np.zeros(size)
time = np.zeros(size)
e_tot = np.zeros(size)
ep_tot = np.zeros(size)
ek_tot = np.zeros(size)
vol = np.zeros(size)

n = -1                                                                                  #list counter, -1 to account for volume not being required from heat file
for file in files:
    m = 0                                                                               #counter for indiv list
    with open(file, 'r') as f:
        text = f.read()
        results = re.split('RESULTS|A V E R A G E S', text)[1]                          #reads data from results section
        lines = results.split('\n')
        for i in lines:
            if 'NSTEP' in i:
                k = indiv[m]                                                            #used to add size of previous file to new data point as each file resets NSTEP to 0
                words = i.split()
                n += 1
                np.put(step, n, (float(words[2]) + step[indiv[m]]))                     #data is stored across 3 lines, check output file format
                np.put(time, n, float(words[5]))
                np.put(temp, n, float(words[8]))

            elif 'VOLUME' in i:
                words = i.split()
                np.put(vol, n, float(words[8]))

            elif 'Etot' in i:
                words = i.split()
                np.put(e_tot, n, float(words[2]))
                np.put(ep_tot, n, float(words[8]))
                np.put(ek_tot, n, float(words[5]))
        m += 1


d = {'Step': step, 'Time / PS': time, 'Temp / K': temp, 'Etot': e_tot, 'EKtot' : ek_tot, 'EPtot': ep_tot, 'Volume' : vol}
df = pd.DataFrame(data=d)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)
#df.plot(x = 'Step', y = ['Etot', 'EKtot', 'EPtot'])
#df.plot(x = 'Step', y = 'Temp / k')
df.iloc[(indiv[0]+1):].plot(x = 'Step', y = 'Volume')
plt.show()

