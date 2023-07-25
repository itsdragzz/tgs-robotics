import gpiozero
import time


class motor():
    def __init__(self):
        
        #Setup pins for motor 1
        self.Backward1 = gpiozero.OutputDevice(10) # On/Off output
        self.Forward1 = gpiozero.OutputDevice(9) #On/Off output
        self.SpeedPWM1 = gpiozero.PWMOutputDevice(11) # set up PWM pin
        #Setup pins for motor 2
        self.Backward2 = gpiozero.OutputDevice(13) # On/Off output
        self.Forward2 = gpiozero.OutputDevice(19) #On/Off output
        self.SpeedPWM2 = gpiozero.PWMOutputDevice(26) # set up PWM pin
        #Setup pins for motor 3
        self.Backward3 = gpiozero.OutputDevice(14) # On/Off output
        self.Forward3 = gpiozero.OutputDevice(15) #On/Off output
        self.SpeedPWM3 = gpiozero.PWMOutputDevice(18) # set up PWM pin
        #Setup pins for motor 4
        self.Backward4 = gpiozero.OutputDevice(16) # On/Off output
        self.Forward4 = gpiozero.OutputDevice(20) #On/Off output
        self.SpeedPWM4 = gpiozero.PWMOutputDevice(21) # set up PWM pin
        self.Backward1.off()
        self.Forward1.off()
        self.Backward2.off()
        self.Forward2.off()
        self.Backward3.off()
        self.Forward3.off()
        self.Backward4.off()
        self.Forward4.off()
    
        
        
        while True:
            directionFlag = input("set motor direction: ")
            if directionFlag == "back": # if user types "back" change direction of motor
                self.Backward3.on() # Sets Backward Direction pin on
                self.Forward3.off() # Sets Backward Direction pin on
            else:
                self.Backward3.off() # Sets Backward Direction off
                self.Forward3.on()   # Sets Backward Direction pin on
            self.speedFlag = float(input("set speed (between 0-1000): ")) # Gets a number from the from the user
            self.SpeedPWM3.value = self.speedFlag/1000 # Sets the duty cycle of the PWM between 0-1