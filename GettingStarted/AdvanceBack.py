#!/usr/bin/env python3

import time
import trilobot

tbot = Trilobot()
exit_now = False
button_names = ["A", "B", "X", "Y"]
last_state = {'A': False, 'B': False, 'X': False, 'Y': False}
new_state = last_state.copy()
delta_state = last_state.copy()


while not exit_now:
    for i in range(NUM_BUTTONS):
        btn_name = button_names[i]
        new_state[btn_name] = tbot.read_button(i)
        delta_state[btn_name] = (new_state[btn_name] != last_state[btn_name] )
        last_state[btn_name] = new_state[btn_name]

    if (new_state["X"]):
        print("X --> Exit")
        exit_now = True
    elif (new_state["Y"] and delta_state["Y"]):
        print("Y --> Stop")
        tbot.stop()
    elif (new_state["A"] and delta_state["A"]):
        print("A --> Advance")
        tbot.forward()
    elif (new_state["B"] and delta_state["B"]):
        print("B --> Backward")
        tbot.backward()
        
    time.sleep(0.5)
