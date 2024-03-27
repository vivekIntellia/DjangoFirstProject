import requests

endpoints ="http://127.0.0.1:8000/services_api/"
getresponse = requests.get(endpoints)
print(getresponse.status_code)
