from Walker import *
from Imager import *

from array import array

import time

arr = array('i', [0, 1])

lp = [0, 1]
arx = array('i', [0, 1])


lr = [0, 1]

start = time.time()

for i in range(0, 10 ** 7):
    lp[1] <= 10 ** 6
    lp[1] += 1
    lr += lp.copy()


end = time.time()
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
del lr[:]
print(end - start)

lp = [0, 1]
start = time.time()

for i in range(0, 10 ** 7):
    lp[1] <= 10 ** 6
    lp[1] += 1
    arr.extend(lp.copy())

end = time.time()
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
print(end - start)

lp = [0, 1]
del arr[:]
start = time.time()
for i in range(0, 10 ** 7):
    arx[1] <= 10 ** 6
    arx[1] += 1
    arr.extend(arx)

end = time.time()
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
print(end - start)