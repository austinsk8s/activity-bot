#!/usr/bin/python2.7
#PiLO.py
#Python version of PiLo
import serial
import time

class PiLo:

    def __init__(self):
        print("Loading up serial communication...")
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=19200)
        print("waiting for port to come online")
        time.sleep(1)
        if self.ser.isOpen:
            print("Port is working")
        else:
            print("Could not establish, please check the pins are in the right sockets and the EEPROM has been set correctly")
            exit(1)

    def sendLine(self, l):
        output= ""
        for c in l:
            output += c
            if len(output) == 8:
                self.ser.write(output.encode('utf-8'))
                self.ser.flush()
                output = ""
                time.sleep(0.000001)
        self.ser.write(output.encode('utf-8'))
        self.ser.flush()

    def sendCommand(self, t, l, r):
        print("Command type: " + ["TICK","SPEED"][t])
        com = ["MOVE","GO"][t] + ":{}:{}\r".format(l, r)
        self.sendLine(com)

        return com

if __name__ == "__main__":
    p = PiLo()

    ticksPerRotation = 64
    wheelCircumference = 208

    MMPerFoot = 304.8
    
    p.sendCommand(0, 1, 1) #this shouldnt move the robot, but will warm up the servos
    
    # 8 foot line
    desiredDistanceInFeet = 8
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)
    
    # 12 foot line
    desiredDistanceInFeet = 12
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # 16 foot line
    desiredDistanceInFeet = 16
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)


    # 6 inch line
    desiredDistanceInFeet = 0.5
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # 12 inch line
    desiredDistanceInFeet = 1
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # 18 inch line
    desiredDistanceInFeet = 1.5
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # 24 inch line
    desiredDistanceInFeet = 2
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    ###############################
    # Differential driving start: #
    ###############################
    
    # 3 feet forward
    desiredDistanceInFeet = 3
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # turn left 90 deg
    desiredRotations = 0.25
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, -ticks, ticks)
    time.sleep(1)

    # 1.5 feet forward
    desiredDistanceInFeet = 1.5
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # turn right 90 deg
    desiredRotations = 0.25
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, -ticks)
    time.sleep(1)

    # 5 feet forward
    desiredDistanceInFeet = 5
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # turn right 90 deg
    desiredRotations = 0.25
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, -ticks)
    time.sleep(1)

    # 4 feet forward
    desiredDistanceInFeet = 4
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # turn right 45 deg
    desiredRotations = 0.125
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, -ticks)
    time.sleep(1)

    # 4 feet forward
    desiredDistanceInFeet = 4
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # turn right 45 deg
    desiredRotations = 0.125
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, -ticks)
    time.sleep(1)

    # 2.5 feet forward
    desiredDistanceInFeet = 2.5
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # do something JFC

    # turn left 90 deg
    desiredRotations = 0.25
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, -ticks, ticks)
    time.sleep(1)

    # 1.5 feet forward
    desiredDistanceInFeet = 1.5
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)
    
    # turn left 90 deg
    desiredRotations = 0.25
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, -ticks, ticks)
    time.sleep(1)

    # 1.7 feet forward
    desiredDistanceInFeet = 1.7
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    # turn right 30 deg
    desiredRotations = 0.0833333333333
    ticks = round(desiredRotations * ticksPerRotation)
    p.sendCommand(0, ticks, -ticks)
    time.sleep(1)

    # 2.26715681 feet forward
    desiredDistanceInFeet = 2.26715681
    desiredDistanceInMM = desiredDistanceInFeet * MMPerFoot
    desiredRotations = desiredDistanceInMM / wheelCircumference
    ticks = desiredRotations * ticksPerRotation
    p.sendCommand(0, ticks, ticks)
    time.sleep(1)

    print("done")
