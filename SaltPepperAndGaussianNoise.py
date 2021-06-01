import numpy as np


def salt_n_pepper(img):
    noise = np.random.normal(0, 1, size=(img.shape[0], img.shape[1]))
    maxi = np.amax(img)
    mini = np.amin(img)
    img = np.where(np.logical_and(noise >= mini - 0.5, noise <= mini + 0.5), 0, img)
    img = np.where(np.logical_and(noise >= maxi - 0.5, noise <= maxi + 0.5), maxi, img)
    return img


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def gaussian(image, v):
    row, col = image.shape
    mean = 0
    sigma = v
    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    noisy = image + gauss
    return noisy
