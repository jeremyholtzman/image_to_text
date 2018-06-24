# image to text

The ocr_clean.py file takes an image and uses pytesseract's image_to_string function to
turn the image into text.

Written in python2.
The example image is word_doc_for_image.png and it's a screenshot of word_doc_for_image.doc

To run the ocr file from the terminal, run the following command:
python ocr_clean.py -i word_doc_for_image.png

To run the ocr file after blurring it, run:
python ocr_clean.py -i word_doc_for_image.png -p "blur"

The scan.py file takes an image, finds the edges of the object in the image
(assumes only one primary object), warps the object so that it appears as if we are looking
at it from a top-down perspective, and does a little processing work so that it looks
like a piece of paper. The tranform.py file is called in scan.py in order to give the object
that top-down perspective.
