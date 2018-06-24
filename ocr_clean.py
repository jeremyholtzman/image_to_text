# run the file with
# python2 ocr.py -i example_01.png
# or
# python2 ocr.py -i example_01.png --p blur

# import the necessary packages
# Image  class is required so that we can load our input image from disk in PIL format
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# image
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR")
# preprocess : The preprocessing method. This switch is optional and for this tutorial and can accept two values:  thresh  (threshold) or blur
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")

args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# check to see if we should apply thresholding to preprocess the
# Next, depending on the pre-processing method specified by our command line argument,
# we will either threshold or blur the image.
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
print text
os.remove(filename)


# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
