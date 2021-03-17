from walkers import *
from imageGen import *


w = Walker([0, 0], [-1024, 1024, -1024, 1024])

w.basicWalk()
imgGen = ImageGenerator(w.walls, w.path)

imgGen.generateFlat("./generated/4.png")
