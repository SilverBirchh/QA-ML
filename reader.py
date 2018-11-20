from PIL import Image
import pytesseract
import cv2
import os

class Reader(object):
    def __init__(self, image, preprocess):
        # Get the image and convert to greyscale to seperate back and fore ground
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.image = self.preprocess(gray, preprocess)

    def preprocess(self, image, preprocess):
        # should thresholding be applied
        if preprocess == "thresh":
            return cv2.threshold(image, 0, 255,
                                cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # should noise reduction be applied
        elif preprocess == "blur":
            return cv2.medianBlur(image, 3)
        
        else: 
            return image

    def get_text(self):
        # write the grayscale image to disk as a temporary file so we can read it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, self.image)

        # load the image as a PIL/Pillow image, apply OCR, and then delete the file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        return text
