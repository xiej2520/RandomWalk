from walker import Walker
from imager import Imager


w = Walker([0, 0], [-256, 256, -256, 256])
w.random_walk()


imgGen = Imager(w)

imgGen.generate_linear_gradient("./generated/1.png")
imgGen.generate_linear_gradient("./generated/2.png", mode="HSV", start_color=(50,200,200), end_color=(200,255,255))
imgGen.generate_linear_gradient("./generated/3.png", mode="RGB", bg_color=(0,0,0,0), start_color=(255,0,0,0), end_color=(0,255,0,255))
imgGen.generate_linear_gradient("./generated/4.png", mode="HSV", bg_color=(0,0,0), start_color=(0,255,255), end_color=(255,255,255))

w.save("./generated/1.walker")
