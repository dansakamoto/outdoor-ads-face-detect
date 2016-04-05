readFile = "../data/id_list_titles_with_chks.tsv"
writeFile = "../data/unique_titles_with_chks"

lines = []

f = open(readFile, 'r')
g = open(writeFile, 'w')

for line in f:
	#tabLoc = line.find("\t")
	substr = line[line.find("\t"):]
	substr = substr.lower()
	substr = substr.replace("!", "")
	substr = substr.replace(".", "")
	substr = substr.replace("'", "")
	substr = substr.replace(",", "")
	substr = substr.replace("-", "")
	substr = substr.replace(" ", "")
	print(substr)
	if substr not in lines:
		lines.append(substr)
		g.write(line)

f.close()
g.close()

'''
f = open(writeFile, 'w')

for line in lines:
	f.write(line)

f.close()
'''

print("done.")




'''

f = open('../data/uniquetitles.tsv', 'w')


row = ""
for field in fields:
	row += field + "\t"

row += "URL\n"
f.write(row)

with open(urlsFile) as f:
	
	for line in f:
		html_doc = urllib.urlopen(line).read()
		soup = BeautifulSoup(html_doc, 'html.parser')
		metaDict = {}

		for li in soup.find_all("li", "metadataField"):
			metaDict[li.find("div", "metadataLabel").string] = li.find("div", "metadataValue").string
			
		row = ""
		for field in fields:
			if field in metaDict:
				#row += metaDict[field].replace(",", "||") + "\t"
				row += metaDict[field] + "\t"
			else:
				row += "\t"

		row += line
		#row = row[:-1] + "\n"
		g.write(row.replace('"',"''").encode('utf8'))

		itr += 1
		print("Processed " + str(itr) + " of " + urlCount)

f.close()

print("done")
'''