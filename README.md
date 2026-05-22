# RaspberryPi-6DOF-Vision-Pick-and-Place-System
Computer-vision based 6DOF robotic arm system using Raspberry Pi 4B, OpenCV, PCA9685 servo control, and USB webcam-based object detection for autonomous pick-and-place automation.
# Raspberry Pi 6DOF Vision Pick-and-Place System

A computer-vision based robotic automation system using a 6-DOF robotic arm, Raspberry Pi 4B, OpenCV, PCA9685 servo control, and USB webcam-based object detection for autonomous pick-and-place operations.

The system detects box-shaped objects using computer vision, calculates object positioning, and performs automated robotic arm movement sequences including:

* Home positioning
* Object pickup
* Lowering sequence
* Object placement
* Return-to-home workflow

This project combines:

* Embedded systems
* Computer vision
* Robotics control
* Servo coordination
* Real-time automation
* Vision-guided manipulation

---

# Features

* Raspberry Pi 4B based control system
* OpenCV object detection
* USB webcam vision processing
* 6-DOF robotic arm
* PCA9685 servo controller
* Autonomous pick-and-place workflow
* Predefined robotic movement states
* Home-position initialization
* Real-time object tracking
* Servo motion coordination
* Python-based control architecture

---

# Hardware Components

## Controller

* Raspberry Pi 4B

## Vision System

* USB Webcam

## Servo Driver

* PCA9685 PWM Driver

## Actuators

* 6 Servo Motors

## Power System

* External 5V Servo Power Supply

---

# Software Stack

## Languages

* Python

## Libraries

* OpenCV
* NumPy
* Adafruit PCA9685 Library
* SMBus
* Time

---

# Robotic States

The robotic arm operates using predefined motion states:

| State       | Function                 |
| ----------- | ------------------------ |
| Home        | Default resting position |
| Pickup      | Move gripper to object   |
| Lower       | Lower arm for gripping   |
| Grab        | Close gripper            |
| Lift        | Raise object             |
| Drop        | Release object           |
| Return Home | Reset robotic arm        |

---

# Computer Vision Workflow

1. USB webcam captures live frames
2. OpenCV processes image
3. Box-shaped object detected
4. Object center coordinates extracted
5. Arm movement sequence triggered
6. Object picked and placed
7. Arm returns to home position

---

---

# Future Improvements

* Inverse kinematics
* AI-based object classification
* ROS integration
* YOLO object detection
* Multi-object sorting
* Conveyor-belt automation
* Web dashboard control
* Wireless robotic control

---

# Author

Ninad Lokhande

GitHub:
https://github.com/Ninadlokhande/RaspberryPi-6DOF-Vision-Pick-and-Place-System
