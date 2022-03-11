import board

from sensors.ds18b20 import SensorDS18B20

DS18B20 = SensorDS18B20('28-3c01d075c071')

while True:

    print(DS18B20.readTempreatur())