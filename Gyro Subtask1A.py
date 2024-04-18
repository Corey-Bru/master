#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank,follow_for_ms,MediumMotor
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor

#Motors/sensors
Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A
gyro = GyroSensor(INPUT_2)

Motor_C = OUTPUT_C



#Inputs
distance = float(input('Input diastance: '))
num_of_laps = int(input('Input the number of laps: '))


#calculations/constants
velocity = 5.91
time = distance/velocity

#Intializing the robot

#robotDrive.on_for_seconds(SpeedPercent(75), 1)
robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
robotDrive.gyro = GyroSensor()
robotDrive.gyro.calibrate()

#Loops for the number of laps 
for i in range(num_of_laps):
    if(i % 2 == 0):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time/0.001)
    else:
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)
  




