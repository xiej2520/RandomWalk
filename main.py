from Walker import *
from Imager import *
import math

w = Walker([0, 0], [-8192, 8192, -8192, 8192])

import time

start = time.time()

w.randomWalk()
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

imgGen = ImageGenerator(w)

imgGen.generateFlat("./generated/1.png")
import os, psutil; print("RAM usage (MB): " + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
