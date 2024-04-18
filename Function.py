#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_A, OUTPUT_B,OUTPUT_C, SpeedPercent, MoveTank,follow_for_ms
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep
import sys

Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A
gyro = GyroSensor(INPUT_2)
#Initializing the robot 
robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
robotDrive.gyro = GyroSensor()
robotDrive.gyro.calibrate()
medMoter = MediumMotor(OUTPUT_C)




def Drive(distance,degrees): 
    velocity = 5.9055
    time = distance/velocity
    print(degrees)
    robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = degrees, follow_for = follow_for_ms, ms = time / 0.001)


def DriveSlow(distance,degrees):
   
    velocity = 1.9685
    time = distance/velocity
    robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(10), target_angle = degrees, follow_for = follow_for_ms, ms = time / 0.001)

def Reverse(distance,degrees):
    #returns what barcode it reads
    Right_Moter = OUTPUT_B
    Left_Motor = OUTPUT_A
    gyro = GyroSensor(INPUT_2)
    #Initializing the robot 
    robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
    robotDrive.gyro = GyroSensor()
    robotDrive.gyro.calibrate()
    velocity = 1.9685
    time = distance/velocity
    robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-10), target_angle = degrees, follow_for = follow_for_ms, ms = time / 0.001)
def turn(direction,degrees):
        if direction == 'left':
            robotDrive.turn_degrees(SpeedPercent(10),target_angle=89)
            degrees = degrees + 89
        else:
            robotDrive.turn_degrees(SpeedPercent(10),target_angle=-89)
            degrees = degrees - 89
        return degrees




def coordinates(Shelving, Box):
    #Only returns the coordinate system no movement in (x,y) format
    NewCoordinates = [0,0]
    if Shelving == 'A1' or Shelving == 'B1':
        if Shelving =='A1':
            NewCoordinates = [0,9]
        else:
            NewCoordinates = [47,9]
    elif Shelving == 'A2' or Shelving == 'B2':
        if Shelving == 'A2':
            NewCoordinates = [0,33]
        else:
            NewCoordinates = [47,33]
    elif Shelving == 'C1' or Shelving == 'D1':
        if Shelving == 'C1':
            NewCoordinates = [0,57]
        else:
            NewCoordinates = [47,57]
    elif Shelving == 'C2' or Shelving == 'D2':
        if Shelving == 'C2':
            NewCoordinates = [0,81]
        else:
            NewCoordinates = [47,81]

    if (Box > 6) and (Shelving != 'C2' or Shelving != 'D2'):
        Yvalue= NewCoordinates[1] + 24
        NewCoordinates[1] =Yvalue
    if(Box <= 6):
        Yvalue = NewCoordinates[1] + 2
        NewCoordinates[1] = Yvalue
    if (Box == 2 or Box == 8):
        Xvalue = NewCoordinates[0]+6
        NewCoordinates[0] = Xvalue
    elif (Box == 3 or Box == 9):
        Xvalue = NewCoordinates[0]+12
        NewCoordinates[0] = Xvalue
    elif (Box == 4 or Box == 10 ):
        Xvalue = NewCoordinates[0]+18
        NewCoordinates[0] = Xvalue
    elif (Box == 5 or Box == 11):
        Xvalue = NewCoordinates[0] +24
        NewCoordinates[0] = Xvalue
    elif (Box == 6 or Box == 12):
        Xvalue = NewCoordinates[0] + 30
        NewCoordinates[0] = Xvalue

    Newx= NewCoordinates[0]+6
    NewCoordinates[0] = Newx

    return NewCoordinates


def barcode(degrees,box):
    
    def Drive(distance,degrees):
      
        velocity = 15
        time = distance/velocity
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = degrees, follow_for = follow_for_ms, ms = time / 0.001)

    color_sensor= ColorSensor(INPUT_4) #initilize color sesnor

    def move_back(): #moves to black sensor to begin
        Right_Moter = OUTPUT_B
        Left_Motor = OUTPUT_A
        robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
        DriveSlow(5.2,degrees)
        if color_sensor.color != ColorSensor.COLOR_BLACK:

            robotDrive.on(-2,-2)
            while True:
                if color_sensor.color == ColorSensor.COLOR_BLACK:
                    break
                else:
                    continue
            robotDrive.stop



          



        return
    if(box > 6):
        move_back()
        Reverse(0.2,degrees)

    # 1 = black 0 = white
    BarcodeArray = []
    for i in range(1,4):
        if color_sensor.color == ColorSensor.COLOR_BLACK:
            BarcodeArray.append(1)
            print("Black",file=sys.stderr)
        else:
            BarcodeArray.append(0)
            print("White",file=sys.stderr)
        if i != 4:
            if(box > 6):
                Reverse(0.65,degrees)
            elif(box <= 6):
                DriveSlow(0.65,degrees)
        
        sleep(1.5)
        
    if color_sensor.color == ColorSensor.COLOR_BLACK:
            BarcodeArray.append(1)
            print("Black",file=sys.stderr)
    else:
        BarcodeArray.append(0)
        print("White",file=sys.stderr)

    if BarcodeArray == [1,0,0,0] or BarcodeArray == [0,0,0,1]:
        return "Type 1"
    elif BarcodeArray == [1,0,1,0] or BarcodeArray == [0,1,0,1]:
        return "Type 2"
    elif BarcodeArray == [1,1,0,0] or BarcodeArray == [0,0,1,1]:
        return "Type 3"
    elif BarcodeArray == [1,0,0,1]:
        return "Type 4"
    else:
        return "error"
    


def task1(shelving, box):
    degrees = 0
    navigate=coordinates(shelving, box)
    Drive(navigate[1]+1.5,degrees)
    turn('right',degrees)
    Drive(navigate[0]+1,degrees)
    sleep(5)
    Drive(90-navigate[0]+5,degrees)
    turn('right',degrees)
    Drive(navigate[1]+4,degrees)

def task2():
    #robot starts at (102,-6) in inches
    degrees = 0
    Reverse(12,degrees)
    degrees = turn('right',degrees)
    #robot ends at (6,-6) inches 102 - 6 = 96
    Drive(96,degrees)
    degrees = turn('left',degrees)
    DriveSlow(12,degrees)

def task3(box):
    degrees = 0
    DriveSlow(15.5,degrees)
    bar=barcode(degrees, box)
    print(bar, file=sys.stderr)
    print(bar)
    sleep(60)

def task4(direction):
    degrees = 0
    if(direction == 'left'):
        DriveSlow(1,degrees)

        #robotDrive.turn_degrees(SpeedPercent(20),target_angle=89)
    
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = 150)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(5), target_angle = 0, follow_for = follow_for_ms, ms = 3000)
        medMoter.on_for_rotations(SpeedPercent(20),3)

        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = 0, follow_for = follow_for_ms, ms = 500)

        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=-89)

        #Robot is now facing the drop off location for subtask 4
        Drive(21,degrees)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = -89, follow_for = follow_for_ms, ms = 1000)
        medMoter.on_for_rotations(SpeedPercent(20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = -89, follow_for = follow_for_ms, ms = 1000)
    else:
        #Reverse(0.5,degrees)
        robotDrive.turn_degrees(SpeedPercent(20),target_angle=-89)
    
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = -89, follow_for = follow_for_ms, ms = 150)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(5), target_angle = -89, follow_for = follow_for_ms, ms = 2000)
        medMoter.on_for_rotations(SpeedPercent(20),3)

        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = -89, follow_for = follow_for_ms, ms = 450)

        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=89)

        #Robot is now facing the drop off location for subtask 4
        Drive(21,degrees)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = 0, follow_for = follow_for_ms, ms = 700)
        medMoter.on_for_rotations(SpeedPercent(20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = 0, follow_for = follow_for_ms, ms = 1000)

def final(shelving,box,dropOff):
    degrees = 0
    navigate=coordinates(shelving, box)
    Drive(navigate[1]+0.5,degrees)
    degrees = turn('right',degrees)
    Drive(navigate[0]+1,degrees)
    sleep(5)
    barcode(degrees,box)
    if(box <= 6):
        DriveSlow(1,degrees)

        robotDrive.turn_degrees(SpeedPercent(20),target_angle=89)
    
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = degrees, follow_for = follow_for_ms, ms = 150)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(5), target_angle = degrees, follow_for = follow_for_ms, ms = 3000)
        medMoter.on_for_rotations(SpeedPercent(20),3)

        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = degrees, follow_for = follow_for_ms, ms = 500)

        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=-89)
    elif(box>6):
        Reverse(1,degrees)
        robotDrive.turn_degrees(SpeedPercent(20),target_angle=-89)
    
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = degrees, follow_for = follow_for_ms, ms = 150)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(5), target_angle = degrees, follow_for = follow_for_ms, ms = 3000)
        medMoter.on_for_rotations(SpeedPercent(20),3)

        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(-30), target_angle = degrees, follow_for = follow_for_ms, ms = 500)

        robotDrive.turn_degrees(speed=SpeedPercent(20),target_angle=89)
    Drive(90-navigate[0]+5,degrees)
    if(dropOff == 'D'):
        degrees = turn('left',degrees)
        #find distance
        Drive(navigate[1]+4,degrees)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        Reverse(6,degrees)

    elif(dropOff == 'B'):
        degrees = turn('right',degrees)
        Drive(navigate[1]+4,degrees)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        Reverse(6,degrees)
    elif(dropOff == 'C'):
        Reverse(navigate[0]+4.5, degrees)
        degrees = turn('left',degrees)
        Drive(navigate[1]+120,degrees)
        degrees = turn('right',degrees)
        medMoter.on_for_rotations(SpeedPercent(-20),3)
        Reverse(6,degrees)
        Reverse(112, degrees)

    




#task1('A1',12)
#task2()
#sleep(2)
#robotDrive.gyro.reset()
#sleep(2)
#task2()
#task3(7)
task4('left')
#final('C1',5,'C')








