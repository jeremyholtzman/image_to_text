# image to text

The ocr_clean.py file takes an image and uses pytesseract's image_to_string function to
turn the image into text.

Written in python2.
The example image is word_doc_for_image.png and it's a screenshot of word_doc_for_image.doc

To run the ocr file from the terminal, run the following command:
python ocr_clean.py -i word_doc_for_image.png

To run the ocr file after blurring it, run:
python ocr_clean.py -i word_doc_for_image.png -p "blur"
