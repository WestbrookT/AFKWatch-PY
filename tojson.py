import yaml, json, os


files = os.listdir()
i = 11

for file in files:
	if file.endswith('.yml'):
		f = open(file, 'r')
		out = open(str(i) +'.json', 'w')

		data = yaml.load(f)

		json.dump(data, out)
		out.close()
		f.close()
		i += 1


