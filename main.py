import os
import time
import sys
# from gpiozero import Button
import face_unlock
import door_unlock
import keyboard


# button = Button(24)

# os.system("sudo python3 data_server.py &")
# os.system("sudo python nfc_unlock.py &")

while True:
    if input() == "1": # button.is_pressed for raspberry btn
        time.sleep(1)
        result = face_unlock.face_unlock()
        if result["unlock"]:
            door_unlock()
    else:
        os.system("sudo python3 data_server.py &")
        sys.exit()

