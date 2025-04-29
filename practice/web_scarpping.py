import requests
import bs4


# hit the web url to get the web page
result = requests.get('https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam')
# to format data in xml format
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup.select('title')[0].getText())

# to get a list of all element which have the given class
elements = soup.select('.vector-toc-text')
# for item in elements:
#     print(item.text)

# get image url and download the images
image = soup.select('img')
for item in image:
    if '250px-A._P._J._Abdul_Kalam.jpg' in item.attrs['src']:
        print(item.attrs['src'])
        # get the image link
        photo = requests.get('https:' + item.attrs['src'])
        print(type(photo))
        # we need to take mode as wb , because we will be writing in binary data into the file
        f = open('apj.jpg', 'wb')
        f.write(photo.content)
