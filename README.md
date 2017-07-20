# manga-download

Downloads images from http://www.mangareader.net as jpeg images using Beautiful Soup and Requests. It can also be used to download images from another website as long as the source code of the website is similar to mangareader. You can view source using your browser.

## Getting Started

### Prerequisites
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](http://docs.python-requests.org/en/master/)

### To Use
Change the url to the name of the series you to download (in this case, berserk)
```
url = 'http://www.mangareader.net/berserk/1'
```
Add the last page number you want to download it till ('chapter/page')
```
while not url.endswith('2/5'):
```
Create a folder where all the images will be stored. Use the folder name here 
```
image = open(os.path.join('folder_name', os.path.basename(mangaUrl)), 'wb')
```

## References
Automate the Boring Stuff with Python: Practical Programming for Total Beginners (by Al Sweigart)
