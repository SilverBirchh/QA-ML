import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number to make identification easier
# The data here is provided by UCI Machine Learning Repository
# The data file contains 20000 lines where the first column is the alphabet
# Following this the 16 columns after this our the features of each character 
# This includes height, width etc.
data= np.loadtxt('openCV/letter-recognition.data', dtype= 'float32', delimiter = ',',
                    converters= {0: lambda ch: ord(ch)-ord('A')})

# Half the data, 10000 for the training data and 10000 for the test data
training_data, testing_data = np.vsplit(data,2)

# Need to remove the actual responses and labels from the data to separate arrays
responses, trainData = np.hsplit(training_data,[1])
labels, testData = np.hsplit(testing_data,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=5)

correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print accuracy