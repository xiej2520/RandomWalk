from walker import Walker
from imager import Imager
import time
import os, psutil;
import matplotlib.pyplot as plt

path_lengths = []
speed1 = []
mem1 = []
speed2 = []
mem2 = []

for i in range(0, 10):
    w = Walker([0, 0], [-512, 512, -512, 512])
    start = time.time()
    w.random_walk()
    path_lengths.append(len(w.path))
    end = time.time()
    speed1.append(float(end - start))
    mem1.append(float(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))

    imgGen = Imager(w)
    start = time.time()
    imgGen.generate_flat("./generated/benchmark.png")
    end = time.time()
    speed2.append(float(end - start))
    mem2.append(float(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))


plt.plot(path_lengths, speed1, 'o')
plt.show()
plt.plot(path_lengths, mem1, 'o')
plt.show()
plt.plot(path_lengths, speed2, 'o')
plt.show()
plt.plot(path_lengths, mem2, 'o')
plt.show()

f = open("./generated/benchmark.txt", "w")
for i in range(0, len(path_lengths)):
    f.write(str(path_lengths[i]) + " " + str(speed1[i]) + " " + str(mem1[i]) + " " + str(speed2[i]) + " " + str(mem2[i]) + "\n")
f.close()