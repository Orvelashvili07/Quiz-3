import json
import requests
import sqlite3


user = input("გთხოვთ, დაასახელეთ ქალაქის სახელი: ")


key = '7c243f74e0eb49dc9249c3ca95c69c40'
url = f'https://api.openweathermap.org/data/2.5/weather?q={user}&appid={key}'
request_serverrr = requests.get(url)


#request მოდულის გამოყენებით ვიყენებ ფუნქციებს-ატრიბუტებს
r_to_ser = request_serverrr
print(r_to_ser)

print("Status Code:", request_serverrr.status_code)
print("reqq", request_serverrr.request)
print("Header:", request_serverrr.headers)
print("His", request_serverrr.history)
print("Texx", request_serverrr.text)



#აქ შემოვიღე json და ფუნქციების გამოყენებით გამომაქვს აღნიშნული ინფორმაციები
serveriss_dicttttt = json.loads(request_serverrr.text)

print("Coordinates:", serveriss_dicttttt['coord'])
print("Weather in City:", serveriss_dicttttt['weather'])

m = serveriss_dicttttt['main']
temp = m['temp']
print('Temp:', temp, 'Min Temperature')

s = serveriss_dicttttt['sys']
country = s['country']
print('Country is:', country)


#აქ შემოვიღე json, რის მიხედვითაც გამოაქვს სტრუქტურული ინფორმაციის სახით
print(json.dumps(serveriss_dicttttt, indent=4))

#აქ შევქმენი ცხრილი სადაც შევინახე ინფორმაცია, და შეიძლება დამატება ცხრილში
conn = sqlite3.connect('amidiii.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE AMINDI
(temp integer,
country varchar(20));
''')





conn.close()


