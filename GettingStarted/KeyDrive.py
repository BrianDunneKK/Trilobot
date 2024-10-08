#!/usr/bin/env python3

import time
import trilobot
from sshkeyboard import listen_keyboard

tbot = trilobot.Trilobot()
exit_now = False


def press(key):
    print(f"'{key}' pressed")

def release(key):
    print(f"'{key}' released")

listen_keyboard(
    on_press=press,
    on_release=release,
)