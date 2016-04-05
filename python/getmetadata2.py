from bs4 import BeautifulSoup
import urllib

urlsFile = "../data/urls_missing_metadata"
urlCount = 0
itr = 0
fields = ['Item ID', 'Description', 'Source Collection', 'Product', 'Medium', 'Placement Company', 'Title', 'Company', 'Date', 'Setting', 'Genre', 'Tone', 'Type', 'Subject', 'Copyright & Usage', 'Spatial Coverage', 'Extent', 'Descriptions']

f = open(urlsFile, 'r')
urlCount = sum(1 for line in f)
urlCount = str(urlCount)
f.close()

g = open('../data/metadata2.tsv', 'w')

row = ""
for field in fields:
	row += field + "\t"

row += "URL\n"
g.write(row)

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

g.close()

print("done")