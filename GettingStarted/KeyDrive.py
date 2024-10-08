#!/usr/bin/env python3

import time
import trilobot
import sshkeyboard

tbot = trilobot.Trilobot()
exit_now = False
speed = 9  # Use keys 0..9, where 9 is max speed


def press(key):
    if (key == "f"):
        print("Forward")
        tbot.forward()
    elif (key == "b"):
        print("Backward")
        tbot.backward()
    elif (key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        speed = int(key)
        print(f"Set speed to '{speed}'")

sshkeyboard.listen_keyboard(on_press=press)