import gpioexp
import wiringpi
import math
import random
from time import sleep
# scp gpioexp.py pi@192.168.0.101:/home/pi/prog
# scp index.py pi@192.168.0.101:/home/pi/prog

exp = gpioexp.gpioexp()
b = {
    3: [994, 1017],
    4: [993, 1016],
    5: [993, 1016]
}

def angle(angle, bounds):
    mapped = angle / 180.0
    dif = bounds[1] - bounds[0]
    res = mapped * dif
    # return bounds[0] + math.floor(dif * mapped)
    # return bounds[0] + math.ceil(dif * mapped)
    return bounds[0] + round(dif * mapped)

def all(pins, apins): 
    exp.pwmFreq(50)
    # abounds = [995, 1017]
    # abounds = [994, 1017]
    # bounds = [994, 1017]
    
    for p in pins:
        exp.analogWrite(p, angle(90.0, b[p]))
    for p in apins:
        exp.analogWrite(p, angle(90.0, b[p]))
    print('middle', angle(90.0, b[p]))
    sleep(1)

    for p in pins:
        exp.analogWrite(p, angle(0.0, b[p]))
    for p in apins:
        exp.analogWrite(p, angle(0.0, b[p]))
    print('begin', angle(0.0, b[p]))
    sleep(1)

    for p in pins:
        exp.analogWrite(p, angle(180.0, b[p]))
    for p in apins:
        exp.analogWrite(p, angle(180.0, b[p]))
    print('end', angle(180.0, b[p]))
    sleep(1)

    i = 0
    while i < 24:
        ang = 60.0
        if i % 2 != 0:
            ang = random.random() * 180.0
        for p in pins:
            exp.analogWrite(p, angle(ang, b[p]))
        for p in apins:
            exp.analogWrite(p, angle(ang, b[p]))
        sleep(0.2)
        print('ANGLE', ang)
        i += 1
    for p in pins:
        exp.analogWrite(p, 0)

def test(freq):
    exp.pwmFreq(freq)
    i = 1537.0
    while i < 1537.02:
        exp.analogWrite(8, i)
        print(i)
        sleep(1)
        exp.analogWrite(8, 0)
        i += 0.001
def test2(freq):
    exp.pwmFreq(freq)
    i = 0.01
    print(exp.analogRead(8))
    while i <= 1:
        exp.analogWrite(8, i)
        print(i)
        sleep(0.5)
        # exp.analogWrite(8, 0)
        i += 0.01
def test3(freq):
    exp.pwmFreq(freq)
    i = 0
    while i < 10:
        val = random.random()
        print(val)
        exp.analogWrite(8, val)
        print(i, exp.analogRead(8))
        sleep(3)
        i += 1

cache = {
    'x': 0,
    'y': 0,
    'z': 0
}
def joystick(jpins, pins, apins):
    exp.pwmFreq(50)
    f = "{0:.2f}"
    x = float(f.format(exp.analogRead(jpins[0])))
    y = float(f.format(exp.analogRead(jpins[1])))
    z = float(f.format(exp.digitalRead(jpins[2])))
    print('x', x, 'y', y, 'z', z)

    # if math.fabs(cache['x'] - x) > 0.1:
    #     cache['x'] = x
    # else:
    #     # for p in pins:
    #     #     exp.analogWrite(p, 0)
    #     # for p in apins:
    #     #     exp.analogWrite(p, 0)
    #     return
    exp.analogWrite(6, y)
    print('angle', x * 180)
    for p in pins:
        exp.analogWrite(p, angle(x * 180, b[p]))
    for p in apins:
        exp.analogWrite(p, angle(x * 180, b[p]))