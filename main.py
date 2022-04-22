import os
import time

from gpiozero import Button
import face_unlock
import door_unlock
import keyboard


# button = Button(24)

# os.system("sudo python data_server.py &")
# os.system("sudo python nfc_unlock.py &")

while True:
    if keyboard.is_pressed("f") == True: # button.is_pressed for raspberry btn
        time.sleep(1)
        result = face_unlock.face_unlock()
        if True == result["unlock"]:
            door_unlock()




