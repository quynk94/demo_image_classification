from matplotlib import pyplot as plt
import cv2


filePath = 'mydata_train.txt'
checkPathPass = 'check_train_pass.txt'
checkPathFail = 'check_train_fail.txt'

f = open(checkPathPass, 'r')
checkContentPass = f.read()
f.close()

with open(filePath) as fp:
    line = fp.readline()
    cont = True
    while line and cont:
        line = fp.readline()
        if len(line) < 10:
            next
        imagePath, positions = line.split()
        if imagePath in checkContentPass:
            next
        xMin, yMin, xMax, yMax, classValue = tuple(positions.split(','))
        image = cv2.imread(imagePath)
        cv2.rectangle(image, (int(xMin), int(yMin)),
                      (int(xMax), int(yMax)), (0, 0, 255), 3)
        cv2.imshow('Rec', image)
        while True:
            k = cv2.waitKey(1000) & 0xFF
            if k == ord('s'):
                print(imagePath)
                cv2.destroyAllWindows()
                cont = False
                f = open(checkPathFail, 'a')
                f.write("%s\n" % (imagePath))
                f.close()
                break
            elif k == ord('n'):
                cv2.destroyAllWindows()
                f = open(checkPathPass, 'a')
                f.write("%s\n" % (imagePath))
                f.close()
                break
