from matplotlib import pyplot as plt
from skimage import color, io, feature


def plotImages(images, grid=(2, 2), figsize=(15, 9), **kwargs):
    f, ax = plt.subplots(grid[0], grid[1], figsize=figsize)
    for imageIdx, (title, image) in enumerate(images.items()):
        if grid[0] == 1:
            ax[imageIdx].set_title(title)
            ax[imageIdx].imshow(image, **kwargs)
            ax[imageIdx].axis('off')
        else:
            ax[imageIdx//grid[0]][imageIdx%grid[1]].set_title(title)
            ax[imageIdx//grid[0]][imageIdx%grid[1]].imshow(image, **kwargs)
            ax[imageIdx//grid[0]][imageIdx%grid[1]].axis('off')
    return f, ax

def loadImage(imagePath, gray=False):
    image = io.imread(imagePath)
    if gray and len(image.shape) > 2:
        image_gray = image
        if image.shape[2] == 4:
            image_gray = color.rgba2rgb(image_gray)
        image_gray = color.rgb2gray(image_gray)
        return image_gray
    return image

def imageToGray(image):
    image = image.copy()
    if len(image.shape) > 2:
        if image.shape[2] == 4:
            image = color.rgba2rgb(image)
        image = color.rgb2gray(image)
    return image

def plotDescriptors(images, grid=(2, 2), figsize=(15, 9), **kwargs):
    f, ax = plt.subplots(grid[0], grid[1], figsize=figsize)
    for imageIdx, (title, args) in enumerate(images.items()):
        if grid[0] == 1:
            ax[imageIdx].set_title(title)
            feature.plot_matches(ax[imageIdx], *args, **kwargs)
            ax[imageIdx].axis('off')
        else:
            ax[imageIdx//grid[1]][imageIdx%grid[1]].set_title(title)
            feature.plot_matches(ax[imageIdx//grid[1]][imageIdx%grid[1]], *args, **kwargs)
            ax[imageIdx//grid[1]][imageIdx%grid[1]].axis('off')
    return f, ax