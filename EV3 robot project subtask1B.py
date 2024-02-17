#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor

#Motors
Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A

#Gyro Sensor


#Whatever final velocty is
velocity = 25
turning_time = 1.15
#Inputs  
distance= float(input('Input a distance for the robot to travel: '))
num_of_laps = int(input('Input the number of laps: '))

#calculations
time_forward=distance/velocity

#loop for the number of laps 
for i in range(num_of_laps):
    if(i%2 == 0):
        tank_drive = MoveTank(Right_Moter,Left_Motor);tank_drive.on_for_seconds(SpeedPercent(50),SpeedPercent(49),time_forward)
    else:
        tank_drive = MoveTank(Right_Moter,Left_Motor);tank_drive.on_for_seconds(SpeedPercent(50),SpeedPercent(49),time_forward)
    tank_drive = MoveTank(Right_Moter,Left_Motor);tank_drive.on_for_seconds(SpeedPercent(-50),SpeedPercent(50),turning_time)
