import json
import requests
#kafka라이브러리를 import합니다.
#from kafka import KafkaProducer
cityId = []
#kafka와 연결
#producer = KafkaProducer(bootstrap_servers=['kafka001:9092'])
apiaddress = "https://api.openweathermap.org/data/2.5/weather?id="
apiKey = "&APPID=6198a2c9222ed9081dc963c0f50656df"
f= open("citylist.json", 'r')
lines = f.readlines()
for line in lines:
    if line.find('"id"')!=-1:
        _id = line[line.find(":")+2:line.find(",")]
        cityId.append(_id)
f.close()
data = {}
for Id in cityId:
    _Url = apiaddress + Id + apiKey
    res = requests.get(_Url)
    data[Id] = res.text
    d = json.loads(str(res.text))
    #api로 받은 데이터를 필요한 것만 추출
    lon = d["coord"]["lon"]
    lat = d["coord"]["lat"]
    temp = d["main"]["temp"]
    temp_min = d["main"]["temp_min"]
    temp_max = d["main"]["temp_max"]
    pressure = d["main"]["pressure"]
    humidity=d["main"]["humidity"]
    windspeed = d["wind"]["speed"]
    winddeg = d["wind"]["deg"]
    dt = d["dt"]
    name=d["name"]
    #사용하기 좋게 key value값으로 정리
    jsonDict = {"lon": lon, "lat": lat, "temp" : temp, "pressure" : pressure
		,"temp_min":temp_min, "temp_max":temp_max
                ,"humidity":humidity,"windspeed":windspeed,"winddeg":winddeg
                ,"dt":dt,"name":name}
    #dumps메서드로 json으로 파싱
    jsonStr = json.dumps(jsonDict)
    print(jsonStr.encode())
    #kafka로 실시간으로 발생한 데이터를 json으로 파싱해서 전송
    #string타입이면 데이터가 넘어갈수 없기 때문에 binary 타입으로 encode
    #producer.send("weather"+str(Id), jsonStr.encode())
#producer.close()
