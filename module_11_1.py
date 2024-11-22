import requests

r = requests.get('https://api.github.com/users/Filtey')
print(r)
print(r.content)
print(r.is_redirect)