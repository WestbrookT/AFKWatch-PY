from keras.layers import Dense
from keras.models import Sequential
from numpy import array
import numpy.random as nr
from conv import label_file_to_list, shuffle_sets
import numpy as np

model = Sequential()

model.add(Dense(input_dim=75, output_dim=50, activation='sigmoid'))
model.add(Dense(output_dim=20, activation='sigmoid'))
model.add(Dense(output_dim=2, activation='sigmoid'))

model.compile(optimizer='RMSprop', loss='mse')

ins, out = label_file_to_list('final.json', [1, 0])
bins, bout = label_file_to_list('bad.json', [0, 1])
ins += bins*3
out += bout*3

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

ins = array(ins)
ins = nonlin(ins)
out = array(out)
out = nonlin(out)

shuffle_sets(ins, out, 4)

from test import bad, good

data = []
data.append(bad)
data.append(good)

data = nonlin(array(data))


hist = model.fit(ins, out, nb_epoch=500, batch_size=64)
#print(hist.history)
print(model.predict(data))