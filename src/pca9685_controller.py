from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

NUM_SERVOS = 6

SERVO_MIN = 0
SERVO_MAX = 180

home_angles = [90, 90, 120, 90, 90, 40]

def set_servo_angle(channel, angle):

    angle = max(SERVO_MIN, min(SERVO_MAX, angle))

    kit.servo[channel].angle = angle

    time.sleep(0.2)

def move_home():

    for i in range(NUM_SERVOS):
        set_servo_angle(i, home_angles[i])

def release_gripper():
    set_servo_angle(5, 80)

def close_gripper():
    set_servo_angle(5, 20)
