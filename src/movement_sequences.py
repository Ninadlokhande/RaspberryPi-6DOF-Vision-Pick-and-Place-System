from pca9685_controller import *
import time

def pickup():

    set_servo_angle(0, 90)

    set_servo_angle(1, 120)

    set_servo_angle(2, 80)

    set_servo_angle(3, 140)

    release_gripper()

    time.sleep(1)

    close_gripper()

    time.sleep(1)

def lower():

    set_servo_angle(1, 140)

    set_servo_angle(2, 60)

    time.sleep(1)

def lift():

    set_servo_angle(1, 90)

    set_servo_angle(2, 110)

    time.sleep(1)

def drop():

    set_servo_angle(0, 40)

    set_servo_angle(1, 120)

    set_servo_angle(2, 80)

    time.sleep(1)

    release_gripper()

    time.sleep(1)

def return_home():

    move_home()
