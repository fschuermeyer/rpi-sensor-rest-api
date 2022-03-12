import time
import board

from datetime import datetime
from tinydb import TinyDB

from sensors.bme280 import SensorBME280
from sensors.dht import SensorDHT
from sensors.ds18b20 import SensorDS18B20

DS18B20 = SensorDS18B20('28-3c01d075c071')
DHT11 = SensorDHT(board.D18,'dht11')
BME280 = SensorBME280(0x77,1015)

data = TinyDB('./sensor.json')

sensorStoreDS18B20 = data.table('ds18b20')
sensorStoreDHT11 = data.table('dht-11')
sensorStoreBME280 = data.table('bme280')

while True:
    sensorStoreDS18B20.insert({"temperatur": DS18B20.readTempreatur(),"time":  datetime.now().strftime("%d-%m-%Y %H:%M:%S")})

    dht_tmp = DHT11.readTempreatur()
    dht_hum = DHT11.readHumidity()

    if dht_tmp and dht_hum:
        sensorStoreDHT11.insert({"temperatur": DHT11.readTempreatur(),"humidity": DHT11.readHumidity(),"time":  datetime.now().strftime("%d-%m-%Y %H:%M:%S")})

    sensorStoreBME280.insert({"temperatur": BME280.readTempreatur(),"humidity": BME280.readHumidity(),"pressure": BME280.readPressure(),"time":  datetime.now().strftime("%d-%m-%Y %H:%M:%S")})

    time.sleep(3)
