# QA Machine Learning Course -  Python OCR

Python Script to read image files and convert them to text using [Google Tesseract](https://github.com/tesseract-ocr/tesseract) and [OpenCV](https://docs.opencv.org/trunk/index.html).

Right now it is a CLI interface. 
Example usage:

`python ocr.py --image images/walmart.jpg`

## Installation 

1. You should have a Python environment set up using Python 2.7 or 3.3. If not set up head [here](https://www.python.org/downloads/) to get it set up.

2. This should also have installed `pip`. Run `pip` in the terminal to see if it did. If it didn't install it you can get it [here](https://www.makeuseof.com/tag/install-pip-for-python/).

3. Clone the project and `cd` in to it. 

4. Install dependencies
```
$ pip install pillow
$ pip install pytesseract
$ pip install numpy
$ pip install opencv-python
```

5. Run the example `python ocr.py --image images/walmart.jpg`

# Credits

Python OCR tutorial https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/


