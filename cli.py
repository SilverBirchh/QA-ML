import argparse
import os

from info import GetInfo
from reader import Reader

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

ocr = Reader(args["image"], args["preprocess"])
text = ocr.get_text()

data = GetInfo(text)

print(data.get_store())
print(data.get_date())
print(data.get_total())

exit()