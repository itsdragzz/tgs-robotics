from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from time import sleep

class distance():
        def __int__(self):
            self.distSensor = PiicoDev_VL53L1X()

            while True:
                self.dist = self.distSensor.read()
                print(str(self.dist) + " mm")
                sleep(0.1)