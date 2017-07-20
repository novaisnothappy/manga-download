import requests, os, bs4

url = 'http://www.mangareader.net/berserk/1'

while not url.endswith('2/5'):

##########
	print('Downloading %s' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)
#########
	mangaElem = soup.select('#img')
	if mangaElem == []:
		print('No image')
	else:
		try:
			mangaUrl = mangaElem[0].get('src')
			res = requests.get(mangaUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			nxtLink = soup.findAll("span", class_="next")
			r = nxtLink[0].find('a')
			url = 'http://www.mangareader.net' + r['href']
			continue
#########
		image = open(os.path.join('berserk', os.path.basename(mangaUrl)), 'wb')
		for chunk in res.iter_content(100000):
			image.write(chunk)
		image.close()
#########
	nxtLink = soup.findAll("span", class_="next")
	r = nxtLink[0].find('a')
	url = 'http://www.mangareader.net' + r['href']

print('Done')
