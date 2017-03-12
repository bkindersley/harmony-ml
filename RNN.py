import numpy as np
#import pandas as pd
from keras.utils import np_utils
from keras.optimizers import SGD
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Dropout, Merge, merge, LSTM


N_CLASSES = 13
P = 0.33
T = 8

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

cat_X = np.asarray(cat_X)
cat_Y = np.asarray(cat_Y)

shuf = np.random.permutation(N)

X = cat_X[shuf, :, :]
Y = cat_Y[shuf, :, :]

train_N = np.ceil(N*(1-P)).astype("int32")

train_X = X[0:train_N,:,:]
train_Y = Y[0:train_N,:,:]

test_X = X[train_N:,:,:]
test_Y = X[train_N:,:,:]

model = Sequential()
model.add(LSTM(20, return_sequences=True, input_shape=(T, N_CLASSES)))
model.add(LSTM(N_CLASSES, return_sequences=True))
#model.add(Activation('softmax'))

sgd = SGD(lr=0.01, momentum=0.1)

model.compile(loss = 'categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(train_X, train_Y, nb_epoch = 10, validation_split=0.1, verbose = 2)

test_res = model.test_on_batch(test_X, test_Y)

print "loss {0}, accuracy {1}".format(test_res[0], test_res[1])








