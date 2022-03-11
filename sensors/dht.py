import adafruit_dht

class SensorDHT: 

    def __init__(self,address,typ):
        self.typ = typ

        if typ == "dht11":
            self.board = adafruit_dht.DHT11(address)
        else:
            self.board = adafruit_dht.DHT22(address)

    def readTempreatur(self):
        return self.board.temperature

    def readHumidity(self):
        return self.board.humidity