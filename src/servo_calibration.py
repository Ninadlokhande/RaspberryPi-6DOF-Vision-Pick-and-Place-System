from pca9685_controller import set_servo_angle
import time

while True:

    servo = int(input("Servo Number: "))

    angle = int(input("Angle: "))

    set_servo_angle(servo, angle)

    time.sleep(0.5)
