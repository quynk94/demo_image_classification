from imutils import paths
import os
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input input")
args = vars(ap.parse_args())

filePath = args['input']
f = open("file_names.txt", "w")

with open(filePath) as fp:
    while True:
        line = fp.readline()
        if len(line) < 10 or ',' not in line:
            break
        imagePath, positions = line.split()
        fileName = imagePath.split(os.path.sep)[-1].split('.')[0]
        f.write(fileName + "\n")
f.close()
