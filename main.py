import os, json
from prune import file_to_list


temp = os.listdir()
files = []

for i in temp:
	if i.endswith('.json'):
		files.append(i)

temp = []
for i in files:

	temp += file_to_list(i)

out = open('final.json', 'w')
json.dump(temp, out)
out.close()



