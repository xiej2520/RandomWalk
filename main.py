from walkers import *
from imageGen import *
"""
w = Walker([0, 0], [-16, 16, -16, 16])

w.basicWalk()

print(w.path)
print(len(w.path))
"""
lengths = []
for i in range(0,10000):
	x = Walker([0,0], [-16, 16, -16, 16])
	x.basicWalk()
	lengths.append(len(x.path))


import numpy as np

xbar = np.mean(lengths)
s = np.std(lengths)
min = np.amin(lengths)
max = np.amax(lengths)
range = max-min
print(xbar, s, min, max, range)

import matplotlib.pyplot as plt

plt.hist(lengths, range)
plt.show()

""" 
1 Million samples for Walker([0, 0], [-16, 16, -16, 16])
mean=302.595826
std=212.4492923014284
min=21
max=3048
"""