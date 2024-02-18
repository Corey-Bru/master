#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank,follow_for_ms
from ev3dev2.sensor import INPUT_1,INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor


#Motors
Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A
gyro = GyroSensor(INPUT_2)


distance = float(input('Input diastance: '))
num_of_laps = int(input('Input the number of laps: '))



velocity = 15
time = distance/velocity

robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
robotDrive.gyro = GyroSensor()
robotDrive.gyro.calibrate()

for i in range(num_of_laps):
     
    if(i == 0):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(30),target_angle=180)
    elif(i == 1):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 180, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(30),target_angle=180)
    elif(i == 2):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 360, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(30),target_angle=180)
    elif(i == 3):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 540, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(30),target_angle=180)
    elif(i==4):
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 720, follow_for = follow_for_ms, ms = time / 0.001)
        robotDrive.turn_degrees(speed=SpeedPercent(30),target_angle=180)