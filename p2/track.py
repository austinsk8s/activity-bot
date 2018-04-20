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
    bot.speedForward(80, 3)
    bot.turnLeft(92)
	time.sleep(2)
    bot.speedForward(80, 1.5)
    bot.turnRight(87)
	time.sleep(2)
    bot.speedForward(80, 5)
    bot.turnRight(90)
	time.sleep(2)
    bot.speedForward(80, 4)
    bot.turnRight(50)
	time.sleep(2)
    bot.speedForward(80, 4)
    bot.turnRight(55)
	time.sleep(2)
    bot.speedForward(80, 2.5)
	bot.speedForwardCircle(80, 0.74 * 80, 5)
    # this next part should be fine
    bot.turnLeft(90)
	time.sleep(2)
    bot.speedForward(80, 2)
    bot.turnLeft(95)
	time.sleep(2)
    bot.speedForward(80, 2)
    bot.turnRight(35)
	time.sleep(2)
    # I'm not sure on this last distance
    bot.speedForward(80, 2.5)
    print("Done")
