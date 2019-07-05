from imutils import paths
import imutils
import cv2
import os
import numpy as np

labels = {
    'blue': 0,
    'red': 1,
    'green': 2,
    'yellow_1': 3,
    'yellow_2': 4
}


def process(dataset):
    imagePaths = list(paths.list_images(dataset))
    imageCount = len(imagePaths)
    print(f'Total {imageCount} images')
    f = open("mydata_train.txt", "r")
    trainData = f.read()
    print(trainData)
    f.close()
    for index, imagePath in enumerate(imagePaths):
        if imagePath not in trainData:
            crop_and_label_images(imagePath, index)


def crop_and_label_images(imagePath, count):
    print("Select roi")
    image = cv2.imread(imagePath)
    imageClone = image.copy()
    data = []
    while True:
        r = cv2.selectROI(imageClone)
        if r[2] == 0 or r[3] == 0:
            break

        print("Select class")
        print("Press ESC to reset")
        print("0 - blue")
        print("1 - red")
        print("2 - green")
        print("3 - yellow_1")
        print("4 - yellow_2")

        k = cv2.waitKey(3000)
        print(k)
        if k % 256 == 48:
            print("Class 0 - blue")
            label = "0"
        elif k % 256 == 49:
            print("Class 1 - red")
            label = "1"
        elif k % 256 == 50:
            print("Class 2 - green")
            label = "2"
        elif k % 256 == 51:
            print("Class 3 - yellow_1")
            label = "3"
        elif k % 256 == 52:
            print("Class 4 - yellow_2")
            label = "4"
        elif k % 256 == 27:
            data = []
            imageClone = image.copy()
            continue
        else:
            print("Too slow")
            continue

        cv2.putText(imageClone, label, (r[0], r[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        cv2.rectangle(imageClone, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]),
                      (0, 0, 255), 3)
        line = str(r[0]) + "," + str(r[1]) + "," + \
            str(r[0]+r[2]) + "," + str(r[1]+r[3]) + "," + str(label)
        data.append(line)

    if len(data) > 0:
        f = open("mydata_train.txt", "a+")
        f.write("%s %s\n" %
                (imagePath, " ".join(data)))
        f.close()
