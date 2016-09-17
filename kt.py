from keras.layers import Dense
from keras.models import Sequential
from numpy import array
import numpy.random as nr
from conv import label_file_to_list, shuffle_sets
import numpy as np

model = Sequential()

model.add(Dense(input_dim=75, output_dim=50, activation='tanh'))
model.add(Dense(output_dim=50, activation='tanh'))
model.add(Dense(output_dim=2, activation='tanh'))

model.compile(optimizer='RMSprop', loss='mse')

ins, out = label_file_to_list('final.json', [1, 0])
bins, bout = label_file_to_list('bad.json', [0, 1])
print(len(bins), len(bins)*4)
ins += bins * 4
out += bout * 4


def nonlin(x, deriv=False):
	# if(deriv==True):
	#     return x*(1-x)
	# return 1/(1+np.exp(-x))
	return np.tanh(x)


ins = array(ins)
ins = nonlin(ins)
out = array(out)

shuffle_sets(ins, out, 4)



test_in = ins[11000:]
test_out = out[11000:]

ins = ins[:11000]
out = out[:11000]

hist = model.fit(ins, out, nb_epoch=500, batch_size=64)
# print(hist.history)
predictions = model.predict(test_in)


def cmp(li):
	if li[0] > li[1]:
		#not cheating
		return 0
	#cheating
	return 1


right = 0
wrong = 0
cheaty = 0
for i, predict in enumerate(predictions):
	if test_out[i][0] == 0:
		cheaty += 1
	if cmp(predict) == cmp(test_out[i]):
		right += 1
	else:
		wrong += 1

print("Right: ", right, " Wrong: ", wrong, " Cheaty: ", cheaty)

if right / (right + wrong) > .99:
	model.save('afknet.h5')
