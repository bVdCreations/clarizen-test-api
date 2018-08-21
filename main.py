import requests
from secret_passw import password

user = "bastiaan_van_denabeele@crgl-thirdparty.com"

url_login = "https://api2.clarizen.com/v2.0/services/authentication/login"

'''
//Perform the login operation on the correct data center

curl -d '{userName:"user",password:"****"}' https://api2.clarizen.com/v2.0/services/authentication/login
'''
r = requests.post(url_login, data={'userName':user,'password':password})
print(r.text)

info = r.json()
print(type(info))

url_cal = "https://api2.clarizen.com/V2.0/services/data/getCalendarInfo"
data_cal= {'userId': info.get('userId')}
session_id = info.get("sessionId")
extra_header = {'Authorization': "Session " + session_id}

r2 = requests.get(url_cal,data=data_cal, headers=extra_header)
print(r2.text)