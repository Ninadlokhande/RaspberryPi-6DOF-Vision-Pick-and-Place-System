from vision_detection import detect_box
from object_tracking import calculate_position
from robotic_arm import execute_pick_and_place
from pca9685_controller import move_home

print("Initializing Robotic Arm")

move_home()

while True:

    obj = detect_box()

    if obj:

        cx, cy = obj

        print("Object Detected")

        position = calculate_position(cx, cy)

        print("Target Position:", position)

        execute_pick_and_place(position)
