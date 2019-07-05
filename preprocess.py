from utils import crop_and_label_images
from utils import resize_image
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", required=True,
                    help="path to input dataset")
    args = vars(ap.parse_args())

    resize_image.process(args['dataset'])
    crop_and_label_images.process(args['dataset'])


if __name__ == '__main__':
    main()
