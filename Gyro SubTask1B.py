#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank,follow_for_ms
from ev3dev2.sensor import INPUT_1,INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor


#Motors/sensors
Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A
gyro = GyroSensor(INPUT_2)

#Inputs
distance = float(input('Input diastance: '))
num_of_laps = int(input('Input the number of laps: '))


#Calculations/Constants
velocity = 15
time = distance/velocity

#Initializing the robot 
robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
robotDrive.gyro = GyroSensor()
robotDrive.gyro.calibrate()


#Loop through the number of lengths 
for i in range(num_of_laps):
     
    if(i == 0):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=178)
    elif(i == 1):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 178, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=178)
    elif(i == 2):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 356, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=178)
    elif(i == 3):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 534, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=178)
    elif(i==4):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 712, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=178)