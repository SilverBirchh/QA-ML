import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the digits file and convert it to greyscale so that is is easy to tell letters from the background
digits = cv2.imread('openCV/digits.png')
gray = cv2.cvtColor(digits, cv2.COLOR_BGR2GRAY)

# Break the image up to an array of 5000 20x20 images so that eacheach letter is separated
individual_letters = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# convert to a Numpy array. It size will be (50,100,20,20)
letters = np.array(individual_letters)

# Now we prepare train_data and test_data.
# Splits the list of digits in half 2500 for test and 2500 for training each with each digit equally
# represented
training_letters = letters[:,:50].reshape(-1,400).astype(np.float32) 
test_letters = letters[:,50:100].reshape(-1,400).astype(np.float32)

# Create labels for train and test data
# Creates a 2D array of 2500 digits rangin 0 to 9
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
print len(test_letters)
test_labels = train_labels.copy()

# Initiate kNN
knn = cv2.ml.KNearest_create()

# train the data to create the feature set 
knn.train(training_letters, cv2.ml.ROW_SAMPLE, train_labels)

# then test it with test data for k=5 which looks for the 5 nearest neighbours and classifies them based
# on the majority class
ret,result,neighbours,dist = knn.findNearest(test_letters, k=5)


#To see the error rate compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print accuracy

# save the data
np.savez('knn_data.npz',train=training_letters, train_labels=train_labels)