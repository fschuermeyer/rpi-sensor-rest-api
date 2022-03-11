import os

class SensorDS18B20: 

    def __init__(self,address):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        self.slaveFile = "/sys/bus/w1/devices/%s/w1_slave" % address

    def readTempreatur(self):
        if os.path.exists(self.slaveFile):
            with open(self.slaveFile,'r') as file:
                return "{:.2f}".format(int((file.read().split('t=')[1]).strip()) / 1000)
        
        raise ValueError('No device is connected at the specified address. Sensor: DS18B20')
