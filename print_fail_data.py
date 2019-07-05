from imutils import paths
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input dataset")
args = vars(ap.parse_args())

filePath = 'mydata_train.txt'
f = open(filePath, 'r')
checkContentPass = f.read()
f.close()

imagePaths = list(paths.list_images(args['dataset']))
for imagePath in imagePaths:
    if imagePath not in checkContentPass:
        print(imagePath)
