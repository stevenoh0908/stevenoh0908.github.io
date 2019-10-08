#Requests Tutorial A

import requests
r = requests.get('https://www.google.com')
print(r.text)
print(r.content)

print(r.status_code)
print(r.headers['Content-Type'])
print(r.encoding)
print(r.ok)
