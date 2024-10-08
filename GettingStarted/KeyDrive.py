#!/usr/bin/env python3

import trilobot
import sshkeyboard

tbot = trilobot.Trilobot()

def press(key):
    global speed
    speed = 9  # Use keys 0..9, where 9 is max speed
    if (key == "s"):
        print("Stop")
        tbot.stop()
    elif (key == "c"):
        print("Coast")
        tbot.coast()
    elif (key == "f"):
        print("Forward")
        tbot.forward(speed/9.0)
    elif (key == "r"):
        print("Right (sharp)")
        tbot.turn_right(speed/9.0)
    elif (key == "R"):
        print("Right (curve)")
        tbot.curve_right(speed/9.0)
    elif (key == "l"):
        print("Left (sharp)")
        tbot.turn_left(speed/9.0)
    elif (key == "L"):
        print("Left (curve)")
        tbot.curve_left(speed/9.0)
    elif (key == "b"):
        print("Backward")
        tbot.backward(speed/9.0)
    elif (key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        speed = int(key)
        print(f"Set speed to '{speed}'")

sshkeyboard.listen_keyboard(on_press=press)
