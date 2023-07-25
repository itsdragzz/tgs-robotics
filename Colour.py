from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

class colours():
    def __init__(self):

        self.fruitList = {
            "Apple":20,
            "Carrot":35,
            "Lime":62,
        }

        self.colourSensor = PiicoDev_VEML6040()# To Change which colour sensor, change it to bus=6 instead of default.

        while True:
            ### Example 1: Printing Raw RGB Data
            self.data = self.colourSensor.readRGB()
            self.red = self.data['red'] #Extracting individual RGB values
            self.grn = self.data['green']
            self.blu = self.data['blue']
            #print(str(blu), "Blue", str(grn), "Green", str(red), "Red")
            self.data = self.colourSensor.readHSV()
            self.hue = self.data['hue']
            self.label = self.colourSensor.classifyHue(self.fruitList)
            print(str(self.label) + "  Hue: " + str(self.hue))
            
            sleep_ms(500)