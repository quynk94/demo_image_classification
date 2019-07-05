from imutils import paths
import imutils
import cv2
import os

args = {
    'videos': 'videos',
    'output': 'images'
}


def process():
    videoPaths = list(paths.list_files(args['videos'], validExts=('.mp4')))
    for videoPath in videoPaths:
        cut_images_from_video(videoPath)


def cut_images_from_video(videoPath):
    print(f'Processing {videoPath}')
    count = 0
    camera = cv2.VideoCapture(videoPath)
    # keep looping
    while True:
        # added this line
        camera.set(cv2.CAP_PROP_POS_MSEC, (count*100))
        # grab the current frame
        (grabbed, frame) = camera.read()

        # if we are viewing a video and we did not grab a frame, then we
        # have reached the end of the video
        if not grabbed:
            print(f'Output {count} images')
            break

        frame = imutils.resize(frame, width=1000)

        key = videoPath.split(os.path.sep)[-2]
        dirPath = os.path.sep.join([args["output"], key])

        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        # write the labeled character to file
        outPath = os.path.sep.join([dirPath, "{}.png".format(
            str(count).zfill(6))])
        cv2.imwrite(outPath, frame)

        # increment the count
        count = count + 1
        if count % 50 == 0:
            print(f'Output {count} images')
    camera.release()
