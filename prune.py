import os, json

def dict_to_list(pd):

	return [pd['x'], pd['y'], pd['z'], pd['ya'], pd['pi']]

def is_empty(dataset):
	for i in dataset:
		if i != 0.0:
			return False
	return True


def file_to_list(filename):

	f = open(filename, 'r')
	data = json.load(f)
	f.close()


	max_time = 0
	datalist = []

	outlist = []

	while(str(max_time) in data):
		datalist.append(data[str(max_time)])
		max_time += 1

	temp = []
	for data_dict in datalist:

		temp += dict_to_list(data_dict)
		if len(temp) == 75:
			if not is_empty(temp):
				outlist.append(temp)
			temp = []



	return outlist





