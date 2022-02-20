from numpy import vstack
from process_single import *
import os
from os.path import isfile, join
import h5py


def get_data(dirs, equalize, multicrop, fullview):
    data = []

    for dir in dirs:
        files = [f for f in os.listdir(join(path, dir)) if isfile(join(path, dir, f))]

        for file in files:
            data += process(join(path, dir, file), equalize, multicrop, fullview)

            print(file)

        print('---', dir, '---')

    return data


path = r'C:\Users\mrshu\lynch-room\data'
outfile = r'dataset'

xdirs = ['bathroom', 'bedroom_ideas', 'hallway_ideas', 'kitchen']
ydirs = ['lynch_google', 'lynch_artnet']

xdata = get_data(xdirs, True, False, False)
ydata = get_data(ydirs, True, True, True)

xdata = np.stack(xdata, axis=0)
ydata = np.stack(ydata, axis=0)

print(len(xdata), len(ydata))
if len(xdata) + len(ydata) > 1000:
    print('slishkom mnogo...')
    exit()

with h5py.File(outfile + ".hdf5", "w") as f:
    f.create_dataset('x', data=xdata, compression='gzip')
    f.create_dataset('y', data=ydata, compression='gzip')
