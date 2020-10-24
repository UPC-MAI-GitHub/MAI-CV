import numpy as np
from matplotlib import pyplot as plt
from skimage import color, data, feature, filters, io, transform
from skimage.util import img_as_float

def plotImages(images:dict, title=None, figsize=(15, 9), **kwargs) -> None:
    f, ax = plt.subplots(1, len(images), figsize=figsize)
    if title is not None:
        f.suptitle(title, fontsize=16)
    for imageIdx, (title, image) in enumerate(images.items()):
        ax[imageIdx].set_title(title)
        ax[imageIdx].imshow(image, **kwargs)
        ax[imageIdx].axis('off')
    return f, ax

def plotImageMatrix(images:dict, title=None, grid=(2, 2), figsize=(15, 9), **kwargs) -> None:
    f, ax = plt.subplots(grid[0], grid[1], figsize=figsize)
    if title is not None:
        f.suptitle(title, fontsize=16)
    for imageIdx, (title, image) in enumerate(images.items()):
        ax[imageIdx//grid[0]][imageIdx%grid[1]].set_title(title)
        ax[imageIdx//grid[0]][imageIdx%grid[1]].imshow(image, **kwargs)
        ax[imageIdx//grid[0]][imageIdx%grid[1]].axis('off')
    return f, ax

def loadFloatImage(imagePath):
    image = io.imread(imagePath)
    image = img_as_float(image)
    return image

def loadGrayFloatImage(imagePath):
    image = loadFloatImage(imagePath)
    if image.shape[2] > 3:
        image = color.rgba2rgb(image)
    image = color.rgb2gray(image)
    return image
