from evdev import InputDevice
from select import select

rfid_presented = ""
keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice('/dev/input/event0')

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)

while True:
        r,w,x = select([dev], [], [])
        for event in dev.read():
                if event.type==1 and event.value==1:
                        if event.code==28:
                                if rfid_presented=="0001155844":
                                        # Unlock Door
                                        print("Unlocking Door.")
                                        GPIO.output(13,GPIO.HIGH)
                                        time.sleep(5)
                                        # Lock Door again
                                        print("Locking Door Again.")
                                        GPIO.output(13,GPIO.LOW)
                                else:
                                        print("Access Denied.")
                                rfid_presented = ""
                        else:
                                rfid_presented += keys[ event.code ]