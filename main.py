from Walker import *
from Imager import *

w = Walker([0, 0], [-128, 128, -128, 128])


w.random_walk()
imgGen = Imager(w)
imgGen.generate_random("./generated/1.png")