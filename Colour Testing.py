from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

fruitList = {
    "Apple":20,
    "Carrot":35,
    "Lime":62,
}

colourSensor = PiicoDev_VEML6040()# To Change which colour sensor, change it to bus=6 instead of default.

while True:
    ### Example 1: Printing Raw RGB Data
    data = colourSensor.readRGB()
    red = data['red'] #Extracting individual RGB values
    grn = data['green']
    blu = data['blue']
    #print(str(blu), "Blue", str(grn), "Green", str(red), "Red")
    data = colourSensor.readHSV()
    hue = data['hue']
    label = colourSensor.classifyHue(fruitList)
    print(str(label) + "  Hue: " + str(hue))
    
    sleep_ms(500)