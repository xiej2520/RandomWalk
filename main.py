from Walker import *
from Imager import *
import math

w = Walker([0, 0], [-512, 512, -512, 512])

import time

start = time.time()

w.randomWalk()

imgGen = ImageGenerator(w)

imgGen.generateFlat("./generated/4.png")
