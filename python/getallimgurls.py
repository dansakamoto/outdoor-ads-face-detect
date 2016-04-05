from bs4 import BeautifulSoup
import urllib
from time import sleep


baseURL = "http://library.duke.edu"
galleryURLs = [("/digitalcollections/brennanjohn/?page=",2), ("/digitalcollections/paverjohn/?page=",17), ("/digitalcollections/rcmaxwellco/?page=",471), ("/digitalcollections/oaaaslidelibrary/?page=", 283), ("/digitalcollections/oaaaarchives/?page=", 809)]

itr = 0
urlCount = 0
for collection in galleryURLs:
	urlCount += collection[1]

urlCount = str(urlCount)

f = open('all_image_urls', 'w')

for collection in galleryURLs:
	for i in range(0,collection[1]):
		html_doc = urllib.urlopen(baseURL+collection[0]+str(i+1)).read()
		soup = BeautifulSoup(html_doc, 'html.parser')
		resultsGrid = soup.find(id="resultsGrid")

		while resultsGrid is None:
			print("Error loading page (" + baseURL+collection[0]+str(i+1) + "), trying again in 1 second...")
			sleep(1.0)
			html_doc = urllib.urlopen(baseURL+collection[0]+str(i+1)).read()
			soup = BeautifulSoup(html_doc, 'html.parser')
			resultsGrid = soup.find(id="resultsGrid")

		for link in resultsGrid.find_all('a'):
			f.write(baseURL + link.get('href') + "\n")
		
		itr += 1
		print("Processed " + str(itr) + " of " + urlCount)

f.close()

print("done!")