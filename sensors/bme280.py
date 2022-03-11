
import board
from adafruit_bme280 import basic as adafruit_bme280

class SensorBME280:
    
    def __init__(self,address,sea_level_pressure):  
        self.sensor = adafruit_bme280.Adafruit_BME280_I2C(board.I2C(),address = address)
        self.sensor.sea_level_pressure = sea_level_pressure

    def readTempreatur(self):
        return self.sensor.temperatures

    def readHumidity(self):
        return self.sensor.humidity

    def readPressure(self):
        return self.sensor.pressure