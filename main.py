from Walker import *
from Imager import *
import math

w = Walker([0, 0], [-800, 800, -800, 800])

import time

start = time.time()

w.randomWalk()
print(len(w.path))

imgGen = ImageGenerator(w)

end = time.time()
print(end - start)
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

start = time.time()
imgGen.generateFlat("./generated/4.png")
end = time.time()
print(end - start)
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
