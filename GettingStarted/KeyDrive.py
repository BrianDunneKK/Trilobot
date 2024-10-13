#!/usr/bin/env python3

import time
import datetime
import os
#import os.path
import trilobot
import sshkeyboard

tbot = trilobot.Trilobot()

def press(key):
    global speed
    speed = 5  # Use keys 0..9, where 9 is max speed
    if (key == "z"):
        print("Stop")
        tbot.stop()
    elif (key == "c"):
        print("Coast")
        tbot.coast()
    elif (key == "w"):
        print("Forward")
        tbot.forward(speed/9.0)
    elif (key == "s"):
        print("Backward")
        tbot.backward(speed/9.0)
    elif (key == "a"):
        print("Right (sharp)")
        tbot.turn_right(speed/9.0)
    elif (key == "q"):
        print("Right (curve)")
        tbot.curve_right(speed/9.0)
    elif (key == "d"):
        print("Left (sharp)")
        tbot.turn_left(speed/9.0)
    elif (key == "e"):
        print("Left (curve)")
        tbot.curve_left(speed/9.0)
    elif (key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        speed = int(key)
        print(f"Set speed to '{speed}'")
    elif (key == "p"):
        filename_photo = "./photo-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        print("Take a photograph ... 5 secs pause") 
        os.system("libcamera-still -t 1 -n --output " + filename_photo)
        time.sleep(5)
        if os.path.isfile(filename_photo):
            print("Photo created: " + filename_photo) 
        else:
            print("Photo NOT created: " + filename_photo)
            
        # libcamera-still -t 5000 --datetime -n --timelapse 1000
        # libcamera-still -t 100 --datetime -n
        # libcamera-still -t 1 -n --output photo.jpg ... Takes one photo

print("W-A-S-D=Forward-Left-Backward-Right, Q-E=Curve left-right, Z=Stop, C=Coast, 0-9=Speed(0-100%), P=Photo")

sshkeyboard.listen_keyboard(on_press=press)
