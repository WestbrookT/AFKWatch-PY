import json
from numpy import array
import numpy.random as nr


def label_file_to_list(filename, label: list):

	f = open(filename, 'r')
	data = json.load(f)
	f.close()


	outs = []
	for vector in data:
		outs.append(label[:])

	return data, outs


def shuffle_sets(ins, outs, times):

	state = nr.get_state()
	for i in range(0, times):
		nr.shuffle(ins)
	nr.set_state(state)
	for i in range(0, times):
		nr.shuffle(outs)


