from confluent_kafka import Producer
import json
import requests
import time
p = Producer({'bootstrap.servers': 'localhost:9092'})
while True:
    response1 = requests.get("http://api.openweathermap.org/data/2.5/weather?q=jaipur&appid=**")
    p.produce('weather', key='jaipur', value=response1.text)
