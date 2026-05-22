from movement_sequences import *

def execute_pick_and_place(position):

    print("Moving to pickup position")

    lower()

    pickup()

    print("Lifting object")

    lift()

    print("Moving to drop position")

    if position == "LEFT":
        set_servo_angle(0, 30)

    elif position == "RIGHT":
        set_servo_angle(0, 150)

    else:
        set_servo_angle(0, 90)

    drop()

    return_home()
