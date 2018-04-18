#!/usr/bin/python2.7
#PiLO.py
#Python version of PiLo
import sys
import time
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Bot import Bot

if __name__ == "__main__":

    bot = Bot()

    bot.warmUp()
    time.sleep(5)
    bot.staticForward(3)
    bot.turnLeft(90)
    bot.staticForward(1.5)
    bot.turnRight(90)
    bot.staticForward(5)
    bot.turnRight(90)
    bot.staticForward(4)
    bot.turnRight(45)
    bot.staticForward(4)
    bot.turnRight(45)
    bot.staticForward(2.5)
    # this part needs work
    # you should instead make a new function in Bot.py
    # that works like bot.speedForward(speed, desiredDistanceInFeet),
    # but allows for you to set two separate speeds in
    # timeWritten = self.sendCommand(1, speed, speed) like
    # timeWritten = self.sendCommand(1, leftWheelSpeed, rightWheelspeed)
    # so that the wheels go two separate speeds to make the turn
    # or you could just hard code this part... either way is fine
    bot.staticForward(
    bot.turnRight(45)
    bot.staticForward(0.3125)
    bot.turnRight(45)
    bot.staticForward(0.3125)
    bot.turnRight(45)
    bot.staticForward(0.3125)
    bot.turnRight(45)
    bot.staticForward(0.3125)
    # this next part should be fine
    bot.turnLeft(90)
    bot.staticForward(1.5)
    bot.turnLeft(90)
    bot.staticForward(1.7)
    bot.turnRight(30)
    # I'm not sure on this last distance
    bot.staticForward(2)
    time.sleep(5)
    print("Done")
