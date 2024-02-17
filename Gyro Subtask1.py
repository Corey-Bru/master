#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor

Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A
gyro = GyroSensor()

distance = float(input('Input diastance: '))
velocity = 25
time = distance/velocity

robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor);tank_drive.on_for_seconds(SpeedPercent(50),SpeedPercent(49),time)

gyro.reset.turn_degrees(0)
while distance <= 700:
    correction = 0 - gyro.turn_to_angle()
    robotDrive.drive(250,correction)
    robotDrive.stop()
    Left_Motor.brake()
    Right_Moter.brake()