from Walker import *
import numpy as np
import matplotlib.pyplot as plt


lengths = []
for i in range(0,10**5):
	x = Walker([0,0], [-2, 2, -2, 2])
	x.random_walk()
	lengths.append(len(x.path))


xbar = np.mean(lengths)
s = np.std(lengths)
min = np.amin(lengths)
max = np.amax(lengths)
range = max-min
print(xbar, s, min, max, range)


plt.hist(lengths, np.amax((1, range)))

import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
plt.show()


""" 
1 Million samples for Walker([0, 0], [-16, 16, -16, 16])
mean=302.595826
std=212.4492923014284
min=21
max=3048
"""