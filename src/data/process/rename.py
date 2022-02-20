import os
from os.path import isfile, join
import shutil

path = 'C:\\Users\\mrshu\\lynch-room\\data\\google downloads\\hallway ideas'
newpath = 'C:\\Users\\mrshu\\lynch-room\\data\\hallway_ideas'
start = 0

files = [f for f in os.listdir(path) if isfile(join(path, f))]

for i in range(len(files)):
    shutil.copyfile(join(path, files[i]), join(newpath, '{:03d}.jpg'.format(i)))