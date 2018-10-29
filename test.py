import gpioexp
import wiringpi
import math
import random
from time import sleep
from funcs import exp, joystick, all

pins = [3, 4]
apins = [5]
jpins = [8, 0, 1]
jpin = 8
try:
    i = 0
    # while i < 1000000:
    #     joystick(jpins, pins, apins);
    #     sleep(0.05)
    #     i += 1
    all(pins, apins)
    # test(2000)
    # test2(2000)
    # test3(50)
    for p in pins:
        exp.analogWrite(p, 0)
    for p in apins:
        exp.analogWrite(p, 0)
    exp.reset()
except KeyboardInterrupt:
    for p in pins:
        exp.analogWrite(p, 0)
    for p in apins:
        exp.analogWrite(p, 0)
    exp.reset()