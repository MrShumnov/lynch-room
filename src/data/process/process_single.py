import skimage
from skimage import exposure, measure
from PIL import Image
import numpy as np
import h5py


def crop(arr, multicrop):
    dh = 1024 - arr.shape[0]
    dw = 2048 - arr.shape[1]

    if dw > 0:
        arr = np.pad(arr, ((0, 0), (dw // 2 + dw % 2, dw // 2), (0, 0)), mode='constant', constant_values=(0, 0))
    if dh > 0:
        arr = np.pad(arr, ((dh // 2 + dh % 2, dh // 2), (0, 0), (0, 0)), mode='constant', constant_values=(0, 0))

    h = arr.shape[0]
    w = arr.shape[1]
    dh = 1024 - h
    dw = 2048 - w

    fh = [[-dh // 2, h + dh // 2]]
    if dh < -200 and multicrop:
        fh += [[0, h + dh], [-dh, h]]

    fw = [[-dw // 2, w + dw // 2]]
    if dw < -200 and multicrop: 
        fw += [[0, w + dw], [-dw, w]]

    arrs = []

    for i in fh:
        for j in fw:
            arrs.append(arr[i[0]: i[1], j[0]: j[1]])

    return arrs
    

def process(img_path, equalize, multicrop, fullview):
    # img_path = r'C:\Users\mrshu\lynch-room\data\lynch_artnet\lynch_013.jpg'

    img = Image.open(img_path)
    arr = np.asarray(img)

    if equalize:
        arr = skimage.exposure.equalize_adapthist(arr, clip_limit=0.02)

    arrs = crop(arr, multicrop)

    if fullview and arr.shape[0] > 1024 * 2 or arr.shape[1] > 2048 * 2:
        arr_small = skimage.measure.block_reduce(arr, (2, 2, 1), np.mean)
        arrs += crop(arr_small, multicrop)

    return arrs

    # for i in range(len(arrs)):
    #     img_eq = Image.fromarray((arrs[i] * 255).astype(np.uint8))
    #     img_eq.save('{:02d}.jpg'.format(i))
