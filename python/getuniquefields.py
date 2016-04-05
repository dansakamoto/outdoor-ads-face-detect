from bs4 import BeautifulSoup
import urllib

urlsFile = "all_image_page_urls"
fields = []
urlCount = 0
itr = 0

f = open(urlsFile, 'r')
urlCount = sum(1 for line in f)
urlCount = str(urlCount)
f.close()

with open(urlsFile) as f:
	
	for line in f:
		html_doc = urllib.urlopen(line).read()
		soup = BeautifulSoup(html_doc, 'html.parser')

		for div in soup.find_all("div", "metadataLabel"):
			if div.string not in fields:
				fields.append(div.string)

		itr += 1
		print("Processed " + str(itr) + " of " + urlCount)

g = open('meta_data_fields', 'w')

line = ""
for field in fields:
	line += field + ","

line = line[:-1] + "\n"
g.write(line)

g.close()

print("done")