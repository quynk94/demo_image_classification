from imutils import paths
import imutils
import cv2
import os
import numpy as np


def process(dataset):
    imagePaths = list(paths.list_images(dataset))
    for index, imagePath in enumerate(imagePaths):
        image = cv2.imread(imagePath)
        image = resize_image(image)
        cv2.imwrite(imagePath, image)


def resize_image(image, width=750, height=750, inter=cv2.INTER_AREA):
    # grab the dimensions of the image and then initialize
    # the deltas to use when cropping
    (h, w) = image.shape[:2]
    dW = 0
    dH = 0

    # if the width is smaller than the height, then resize
    # along the width (i.e., the smaller dimension) and then
    # update the deltas to crop the height to the desired
    # dimension
    if w < h:
        image = imutils.resize(image, width=width,
                               inter=inter)
        dH = int((image.shape[0] - height) / 2.0)

    # otherwise, the height is smaller than the width so
    # resize along the height and then update the deltas
    # crop along the width
    else:
        image = imutils.resize(image, height=height,
                               inter=inter)
        dW = int((image.shape[1] - width) / 2.0)

    # now that our images have been resized, we need to
    # re-grab the width and height, followed by performing
    # the crop
    (h, w) = image.shape[:2]
    image = image[dH:h - dH, dW:w - dW]

    # finally, resize the image to the provided spatial
    # dimensions to ensure our output image is always a fixed
    # size
    return cv2.resize(image, (width, height),
                      interpolation=inter)
