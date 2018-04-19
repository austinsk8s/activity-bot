#!/usr/bin/python2.7
from __future__ import division
import serial
import time

class Bot:

    ticksPerRotation    = 64
    wheelCircumference  = 208
    MMPerFoot           = 304.8
    commandSent         = False

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
        self.commandSent = True
        return time.time()


    def commandFinished(self):
        while self.commandSent:
            response = self.ser.readline()

            if len(response) > 0 and "done" in response.lower():
                print("command complete")
                self.commandSent = False
                return True;
            else:
                print(response)
                return False

        return False


    def warmUp(self):
        self.sendCommand(0, 1, 1)

    def sendCommand(self, t, l, r):
        print("Command type: " + ["TICK","SPEED"][t])
        com = ["MOVE","GO"][t] + ":{}:{}\r".format(l, r)
        timeWritten = self.sendLine(com)
        return timeWritten

    def staticForward(self, desiredDistanceInFeet):
        desiredDistanceInMM = desiredDistanceInFeet * self.MMPerFoot
        desiredRotations = desiredDistanceInMM / self.wheelCircumference
        ticks = round(desiredRotations * self.ticksPerRotation)
        self.sendCommand(0, ticks, ticks)


    # speed is the servos ticks/second
    def speedForward(self, speed, desiredDistanceInFeet):
        desiredDistanceInMM = desiredDistanceInFeet * self.MMPerFoot
        desiredRotations = desiredDistanceInMM / self.wheelCircumference
        ticks = desiredRotations * self.ticksPerRotation
        # We must account for the time taken from sending the command to when it is flushed
        timeRequired = ticks / speed
        timeStarted = time.time()
        timeWritten = self.sendCommand(1, speed, speed)
        # And use that value to sleep after going a specific amount of time
        timeToStart = timeStarted - timeWritten
        timeToSleep = timeRequired + timeToStart
        time.sleep(timeToSleep)
        self.sendCommand(1, 0, 0)


    def turnLeft(self, degrees):
        rotations = (degrees / 180) - 0.1
	ticks = round(rotations * self.ticksPerRotation)
        self.sendCommand(0, -ticks, ticks)


    def turnRight(self, degrees):
        rotations = (degrees / 180) - 0.1
        ticks = round(rotations * self.ticksPerRotation)
        self.sendCommand(0, ticks, -ticks)
