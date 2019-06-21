import requests

payload = {
    'name':'arj',
    'password':'1234'
}

headers = {
    'content-type':'/resources/resource.xml',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.151',
    'Request Method':'GET',
    'Accept Encoding':'gzip, deflate',
    'Accept Language':'en-US,en;q=0.9'
}
'''
r = requests.post('http://localhost:5000/protected_by_cookie', data=payload)
print(r.text)
'''

# session.get
#s = requests.Session()
'''
p = requests.post('http://localhost:5000/verify_cookie_login', data=payload)
print(p.text)
'''
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('john', 'matrix')
r = requests.post(url="http://localhost:5000/secret", auth=
auth)
print(r.text)

import requests
files = {'file': open('C:/Users/j/Desktop/entry/git/pymug-june19/backend/pylogo.png', 'rb')}
req = r.post("http://localhost:5000/upload_service", files=files)
print(req.text)

