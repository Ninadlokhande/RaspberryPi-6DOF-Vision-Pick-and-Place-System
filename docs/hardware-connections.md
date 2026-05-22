# Hardware Connections

## Raspberry Pi 4B to PCA9685

| Raspberry Pi Pin | PCA9685 |
| ---------------- | ------- |
| Pin 1 (3.3V)     | VCC     |
| Pin 3 (SDA)      | SDA     |
| Pin 5 (SCL)      | SCL     |
| Pin 6 (GND)      | GND     |

---

# PCA9685 to Servo Connections

| Servo          | Channel   |
| -------------- | --------- |
| Base Servo     | Channel 0 |
| Shoulder Servo | Channel 1 |
| Elbow Servo    | Channel 2 |
| Wrist Pitch    | Channel 3 |
| Wrist Roll     | Channel 4 |
| Gripper        | Channel 5 |

---

# Power Connections

The servo motors are powered using:

* 5V 10A SMPS

The Raspberry Pi is isolated from direct servo current loads.

---

# USB Webcam

The USB webcam connects directly to:

* Raspberry Pi USB Port

and provides real-time image frames for OpenCV processing.
