## 빅데이터의 이해 수업 Termproject
# 기상데이터 실시간 처리 플랫폼
----
# API 요청을 보내면 넘어오는 데이터의 형태
----
![openweathermap_data](/image/1.png)

# 구조도
![diagram](/image/2.png)

# 실시간 데이터 발생(python)
openweathermap사이트에서 제공해주는 도시들의 목록이 닮긴 json파일을 받아서 원하는 도시들의 리스트들만 추려낸 citylist.json파일에서 해당 도시들의 id값들을 읽어와서 requests.get메소드를 이용해서 api 데이터를 받아온다.
위의 스크린샷을 보면 데이터를 받아서 바로 사용하기 번거로운 형태에서 가공을 해줘서 dumps메소드로 json으로 파싱하고 kafka로 전송하기 위해서는 string에서 binary 타입으로 인코딩시켜야 하기때문에 인코딩하고 전송

# Kafka 토픽 리스트 확인
![topiclist](/image/3.png)
weather1833747~weather1845604까지 생성된 토픽들

# Kafka -> Spark & Spark -> Kafka
실행 환경 : intelliJ IDEA
처음 계획으로는 스파크에서 데이터를 분석하려했으나 넘어온 api 데이터로 뭘 처리할지 못찾아서 그냥 구조도 상 거치기만 함

![jar_file](/image/4.png)
생성된 jar파일을 실행할 때 spark-submit에서 package옵션으로 기술해주는 이유는 build.sbt파일에서 dependency를 기술해주는데 이유는 모르지만 dependency가 인식이 안되서 직접 기술 
'''
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.0,org.apache.kafka:kafka_2.12:0.11.0.0 --class Weather --master yarn kafka-wordcount_2.11-0.1.jar
'''

![spark-submit](/image/5.png)
spark를 실행시켜놓고 Crontab으로 api데이터를 받아오는 python파일을 10분에 한번씩 실행되게 등록시킨다. 10분마다 python코드가 실행되면 데이터가 들어오면 spark에서 데이터를 처리 후 kafka로 보낸다.

# Kafka -> node.js
![node.js_1](/image/6.png)
![node.js_2](/image/7.png)
![node.js_3](/image/8.png)
![node.js_4](/image/9.png)
![node.js_5](/image/10.png)
![node.js_6](/image/11.png)

# Webserver -> Webpage
Highcharts라이브러리와 google map API를 이용해서 해당 도시들의 위치에 marker로 표시하고 marker를 클릭하면 infomap이 나와서 도시의 기상 데이터를 보여줍니다. Highcharts에서는 온/습도를 꺾은선 그래프로 표현해줍니다. 
10분마다 크론탭에 등록 된 python코드가 실행되면 새로 데이터가 업데이트되서 실시간으로 처리 됩니다.
시간에 쫓겨서 웹페이지 디자인은 신경을 못썼습니다.
![webpage_1](/image/12.png)
![webpage_2](/image/13.png)