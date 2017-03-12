import numpy as np
#import pandas as pd
from keras.utils import np_utils
from keras.optimizers import SGD
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Dropout, Merge, merge, LSTM


N_CLASSES = 13

raw_data = np.genfromtxt('data/harmonyData.csv', delimiter=',', dtype=np.int32, skip_header = 1)
raw_X = raw_data[:,0:8]
raw_Y = raw_data[:,8:16]

N = raw_data.shape[0]

cat_X = []
cat_Y = []

for i in np.arange(N):
  tmp_x = raw_X[i,:]
  tmp_y = raw_Y[i,:]
  
  cat_x = np_utils.to_categorical(tmp_x, nb_classes = N_CLASSES)
  cat_y = np_utils.to_categorical(tmp_y, nb_classes = N_CLASSES)
  
  cat_X.append(cat_x)
  cat_Y.append(cat_y)

print(np.shape(cat_X))
print(np.shape(cat_Y))



