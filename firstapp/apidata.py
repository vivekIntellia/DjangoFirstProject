import requests
import json

URL ="http://127.0.0.1:8000/services_api/"

data = {
    'title' : 'Python Programming',
    'descritpion' : "Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to get started with Python. Fortunately an experienced programmer in any programming language (whatever it may be) can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!",
    'link' : 'https://www.python.org/about/gettingstarted/'
}

json_data = json.dumps(data)
r = requests.post(url = URL , data = json_data)
data = r.json()
print(data)