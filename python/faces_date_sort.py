import os

allfiles = os.listdir('../isolated_faces_tosort')

unique = []
yearDict = {}

for name in allfiles:
	if name[0:7] not in unique:
		unique.append(name[0:7])
		yearDict[name[0:7]] = 1
	else:
		yearDict[name[0:7]] += 1

f = open('ids_with_faces_and_dates.tsv', 'w')
g = open('../data/metadata.tsv', 'r')

for line in g:
	split = line.split('\t')
	if split[0] in unique:
		if split[8] != 'Undated':
			if split[8] != 'ND':
				ID = split[0]
				yr = split[8]
				ind = yr.find('1')
				i = yearDict[ID]
				for x in range(1, i):
					out = split[0] + "\t" + split[0] + "-" + str(x) + "\t" + yr[ind:ind+4] + "\t" + split[6] + "\n"
					f.write(out)

f.close();
g.close();
