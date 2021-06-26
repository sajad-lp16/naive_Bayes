import requests

url = "https://www.mongard.ir/courses/"
res = requests.get(url)
if res.status_code == 200:
    print('I Got that website')
