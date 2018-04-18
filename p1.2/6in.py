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
    bot.staticForward(0.5)
    time.sleep(5)
    print("Done")
