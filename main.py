from Walker import *
from Imager import *


w = Walker([0, 0], [-1024, 1024, -1024, 1024])
w.random_walk()


imgGen = Imager(w)

imgGen.generate_linear_gradient("./generated/1.png")
imgGen.generate_linear_gradient("./generated/2.png", bg_color=(0,0,0,0), start_color=(255,0,0,255), end_color=(0,255,0,255))
