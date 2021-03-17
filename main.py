from walkers import *
from imageGen import *
import math

w = Walker([0, 0], [-128, 128, -128, 128])

w.randomWalk()
imgGen = ImageGenerator(w)

imgGen.generateRandom("./generated/4.png")