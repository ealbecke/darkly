import httplib2
import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
urls = list()
message_lst = list()

url_input = raw_input("Url du site(ex: 10.12.1.115): ")

def get_href(url):
    status, response = http.request(url)
    soup = BeautifulSoup(response)
    for link in soup.findAll('a'):
        elem = link.get('href')
        if elem == 'README':
            data = urllib2.urlopen(url + elem).read(2000)
            data = data.split("\n")
            message_lst.append(data[0])
        full_url = url + elem
        if elem.find('README') and elem.find('../') and full_url not in urls:
            print(full_url)
            urls.append(full_url)
        if elem.find('../'):
            get_href(full_url)


cnt = get_href('http://' + url_input + '/.hidden/')

#On supprime les doublons de la liste
new_msg = list(set(message_lst))

print('Les differents messages trouve dans les README sont les suivants:')
for elem in new_msg:
    print(elem)

