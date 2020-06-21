import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt
from image_warp import warp_images
# load image as pixel array
image = image.imread('image_for_patches.jpg')


def get_batch(image, w, h, n, pyramid_levels):
    for i in range(pyramid_levels):
        



def get_patch_randomly(image, w, h):
    image_width = image.shape[1]
    image_height = image.shape[0]
    x = np.random.randint(0, image_width - w, dtype=np.int)
    y = np.random.randint(0, image_height - h, dtype=np.int)
    crop = image[y:y+h, x:x+w, :]
    return crop


def get_patches_randomly(image, w, h, n):
    patches = []
    for i in range(n):
        patches.append(get_patch_randomly(image, w, h))

    patches = np.stack(patches, axis=0)
    return patches


def transform_image(image, change_size):
    image_width = image.shape[1]
    image_height = image.shape[0]

    grid_points = []
    transformed_grid_points = []

    for i in range(1, 5):
        for j in range(4):
            x = int((i/4)*image_width)
            y = int((j/4)*image_height)

            grid_points.append((y,x))

            r = np.random.randint(0, 5)

            if r == 0:
                x += change_size
            elif r == 1:
                x -= change_size
            elif r == 2:
                y += change_size
            elif r == 3:
                y -= change_size
            elif r == 4:
                pass

            transformed_grid_points.append((y,x))

    grid_points = np.array(grid_points)
    transformed_grid_points = np.array(transformed_grid_points)
    out_region = [change_size*2, change_size*2, image_height-change_size*2, image_width-change_size*2]
    images = [np.squeeze(image[:, :, i]) for i in range(3)]
    images = warp_images(grid_points, transformed_grid_points, images, out_region)
    image = np.stack(images, axis=2)
    return image







tmp = transform_image(image, 10)
