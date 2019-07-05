import xml.etree.cElementTree as ET
import os
import sys
import argparse
import shutil

sys.path.append(os.path.realpath('.'))

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="path to output xml")
ap.add_argument("-i", "--input", required=True,
                help="path to text file")
args = vars(ap.parse_args())

filePath = args['input']
xmlPath = args['output']


if os.path.exists(xmlPath):
    shutil.rmtree(xmlPath)
    os.mkdir(xmlPath)

with open(filePath) as fp:
    while True:
        line = fp.readline()
        if len(line) < 10 or ',' not in line:
            break
        imagePath, positions = line.split()
        xMin, yMin, xMax, yMax, classValue = tuple(positions.split(','))

        annotation = ET.Element("annotation")

        ET.SubElement(annotation, "folder").text = "VOC2000"
        ET.SubElement(annotation, "filename").text = imagePath.split(
            os.path.sep)[-1]
        ET.SubElement(annotation, "segmented").text = "0"

        size = ET.SubElement(annotation, "size")
        ET.SubElement(size, "width").text = "750"
        ET.SubElement(size, "height").text = "750"
        ET.SubElement(size, "depth").text = "3"

        object_tag = ET.SubElement(annotation, "object")
        ET.SubElement(object_tag, "name").text = "long_blue"
        ET.SubElement(object_tag, "pose").text = "Left"
        ET.SubElement(object_tag, "truncated").text = "1"
        ET.SubElement(object_tag, "difficult").text = "0"

        bndbox = ET.SubElement(object_tag, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(xMin)
        ET.SubElement(bndbox, "ymin").text = str(yMin)
        ET.SubElement(bndbox, "xmax").text = str(xMax)
        ET.SubElement(bndbox, "ymax").text = str(yMax)

        filename = imagePath.split(os.path.sep)[-1].split('.')[0]
        tree = ET.ElementTree(annotation)
        outputPath = "{}/{}.xml".format(
            xmlPath, filename)
        tree.write(outputPath)
