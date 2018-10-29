import time
from RPIO import PWM
servo = PWM.Servo()
# Set servo on GPIO17 to 900.s (0.9ms)
servo.set_servo(17, 900)
# Set servo on GPIO17 to 2000.s (2.0ms)
#servo.set_servo(17, 2000)
# Raspberryzaebal3157
# pscp c:\Users\3cL1p5e7\t.py pi@192.168.0.101:servo.py

def angleMap(angle):
        return int((round((1950.0 / 180.0), 0) * angle) + 550)

try:
        i = 0
        step = 100
        sleep = 0.1
        direction = True
        activated = True
        while activated is True:
                servo.set_servo(17, angleMap(30))
                time.sleep(sleep)
                servo.set_servo(17, angleMap(90))
                time.sleep(sleep)
                servo.set_servo(17, angleMap(150))
                #servo.set_servo(17, 750 + i * 100)
                # activated = False
                # time.sleep(sleep)
                # print 750 + i * 100
                # if direction is True:
                #     i += 1
                # if 750 + i * 100 > 2500:
                #     direction = False
                #     i -= 1
                # if direction is False:
                #     i -= 1
                # if direction is False and i <= 0:
                #     direction = True
                #     i = 0

except KeyboardInterrupt:
        # Clear servo on GPIO17
        servo.stop_servo(17)
