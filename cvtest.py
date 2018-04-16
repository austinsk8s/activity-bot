#!/usr/bin/python2.7
#PiLO.py
#Python version of PiLo
import serial
import time
import sys
from Bot import Bot

if __name__ == "__main__":

    bot = Bot()

    bot.warmUp()
    bot.staticForward(1.5)
    bot.turnLeft(90)
    bot.staticForward(1.5)
    bot.turnLeft(90)
    bot.staticForward(1.5)
    bot.turnLeft(90)
    bot.staticForward(1.5)
    bot.turnLeft(90)

    print("Done")
